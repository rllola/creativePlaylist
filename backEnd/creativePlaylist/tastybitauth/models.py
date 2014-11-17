from django.db import models
from django.contrib.auth.models import User

from django.utils import timezone

# Create your models here.

class BitAuth(models.Model):
    user = models.OneToOneField(User, related_name='x-identity')
    key = models.CharField(max_length=128, blank=True, default='', db_index=True) #this wont be needed, were only using sin
    sin = models.CharField(max_length=128, blank=True, default='', db_index=True)
    nonce = models.BigIntegerField(default=0)
    created = models.DateTimeField(default=timezone.now)

    def __unicode__(self):
        return u"%s" % (self.user)
