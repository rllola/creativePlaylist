from django.contrib.auth.models import AnonymousUser, User
from django.utils import timezone

from tastypie.authentication import Authentication

from tastypie.http import HttpUnauthorized
from tastypie.compat import get_user_model, get_username_field

from tastybitauth.models import BitAuth

#for connecting to node auth server for signature verification until we write some cool python shit
import requests


class BitAuthAuthentication(Authentication):
    """
    Handles bitauth, in which a user provides a public key & one time signature in the header.

    Uses the ``ApiKey`` model that ships with tastypie. If you wish to use
    a different model, override the ``get_key`` method to perform the key check
    as suits your needs.
    """
    def _unauthorized(self):
        print "_unauthorized"
        return HttpUnauthorized()

    def extract_credentials(self, request):
        #print request.META
        if request.META.get('HTTP_X_IDENTITY') and request.META.get('HTTP_X_SIGNATURE') :
            x_identity = request.META['HTTP_X_IDENTITY'] 
            x_signature = request.META['HTTP_X_SIGNATURE'] 

        else:
            return HttpUnauthorized()
            #this throws some weird error#  ValueError("Incorrect authorization headers.")

        return x_identity, x_signature


    def verify_signature(self, data, pubkey, signature):

        try:
            import json
            print "verify_signature"
            payload = {'data': data, 'pubkey': pubkey, 'signature': signature}
            url = 'http://localhost:3000/verifysignature/'
            r = requests.get(url, params=payload)#headers=headers) #, data=json.dumps(payload)
        except:
            return ValueError("where is node?")
        return True


    def get_sin(self, pubkey):

        try:
            import json
            payload = {'pubkey': pubkey}
            url = 'http://localhost:3000/getsin/'
            r = requests.get(url, params=payload)
            print "after request"
        except:
            return ValueError("where is node?")
            
        return r.text


        #all this shit below irrelevant for now
        '''
        from Crypto.Hash import SHA256
        from ecdsa import VerifyingKey, BadSignatureError, SECP256k1
        h = SHA256.new(data)
        #vk = VerifyingKey.from_string(curve)
        vk = VerifyingKey.from_string(pubkey, curve=SECP256k1)
        
        try:
            vk.verify(signature, data)
            print "yay"
            return True
        except BadSignatureError:
            print "yo u cant sign?"
            return False

        #from pybitcointoools import *
        #h = sha256(data)
        '''
       
    
    def is_authenticated(self, request, **kwargs):
        """
        Finds the user and checks their API key.

        Should return either ``True`` if allowed, ``False`` if not or an
        ``HttpResponse`` if you need something custom.
        """

        try:
            x_identity, x_signature = self.extract_credentials(request)
        except ValueError:
            return self._unauthorized()

        if not x_identity or not x_signature:
            return self._unauthorized()

        print "tried with id , sig"
        print x_identity
        print x_signature
        #verify signature against identity
        #done below self.get_verification(x_identity, x_signature)

        #get the sin so we can lookup the user
        thesin = self.get_sin(x_identity)
        print "SIN YO"
        print thesin

        print x_identity
        #lookup the username related to this identity
        username_lookup = self.get_user(thesin)

        if username_lookup and not isinstance(username_lookup, HttpUnauthorized):
            username = username_lookup
        else:
            return self._unauthorized()
        
        print "user"
        print username
        #this shit below seems nessecary for tastypie ... need to investigate
        username_field = get_username_field()
        User = get_user_model()


        
        try:
            lookup_kwargs = {username_field: username}
            user = User.objects.get(**lookup_kwargs)
        except (User.DoesNotExist, User.MultipleObjectsReturned):
            return self._unauthorized()

        #no unactive users here pls
        if not self.check_active(user):
            return False
        

        #validate the signature against public key in our db and authorize the request against 
        key_auth_check = self.verify_signature("http://localhost:8000/api/v1/user/", x_identity, x_signature)
        if key_auth_check and not isinstance(key_auth_check, HttpUnauthorized):
            request.user = user
            print request.user

        return key_auth_check

    def get_user(self, sin):
        
        try:
            print 'authrecord'
            print sin
            authrecord = BitAuth.objects.get(sin=sin)
            print authrecord

        except BitAuth.DoesNotExist:
            return self._unauthorized()
        return authrecord


   
    def get_identifier(self, request):
        """
        Provides a unique string identifier for the requestor.

        This implementation returns the user's x-signature.
        
        This get_identifier optional, will look more into it
        """
        print "Pute identifier"
        x_identity, x_signature = self.extract_credentials(request)
        return x_identity or 'noid'
