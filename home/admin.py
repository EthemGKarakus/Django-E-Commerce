from django.contrib import admin

# Register your models here.
from home.models import Setting, ContactMessage


class SettingAdmin(admin.ModelAdmin):
    list_display = ['name', 'company','status']
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'subject','status']
    readonly_fields = ('name', 'subject',"email","message","ip")
    list_filter = ["status"]


admin.site.register(Setting,SettingAdmin)
admin.site.register(ContactMessage,ContactMessageAdmin)