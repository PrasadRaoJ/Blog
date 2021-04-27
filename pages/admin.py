from django.contrib import admin

# Register your models here.
from .models import Contact 


class ContactAdmin(admin.ModelAdmin):
    list_display = ('name','email','subject','contacted_at','is_resolved')
    list_filter = ('contacted_at','is_resolved',)
    list_editable = ('is_resolved',)

admin.site.register(Contact, ContactAdmin)
