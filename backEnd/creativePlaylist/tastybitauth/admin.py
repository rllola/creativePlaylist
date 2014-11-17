from django.contrib import admin

# Register your models here.

from tastybitauth.models import BitAuth

class BitAuthAdmin(admin.ModelAdmin):
    list_display = ('user', 'sin',)
    raw_id_fields = ('user',)
    autocomplete_lookup_fields = {
        'fk': ['user_id'],
    }


admin.site.register(BitAuth, BitAuthAdmin)