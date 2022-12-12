from django.contrib import admin
from django.utils.html import format_html
from .models import Speaker, Contact, Talk, Course

# Register your models here.


class ContactInLine(admin.TabularInline):
    model = Contact
    extra = 1

class SpeakerAdmin(admin.ModelAdmin):
    inlines = [ContactInLine]
    prepopulated_fields = {'slug': ('name',)}
    list_display = ['name', 'photo_img', 'website_link', 'email', 'phone']

    def website_link(self, obj):
        return format_html('<a href="{0}" target="_blank">{0}</a>', obj.website)

    def photo_img(self, obj):
        return format_html('<img width="32px" src="{}"/>', obj.photo)

    def email(self, obj):
        return obj.contact_set.emails()[0]
        return Contact.emails.filter(speaker=obj).first()
        return Contact.objects.filter(kind=Contact.EMAIL, speaker=obj).first()

    def phone(self, obj):
        return obj.contact_set.phones().first()
        return Contact.phones.filter(speaker=obj).first()
        return Contact.objects.filter(kind=Contact.PHONE, speaker=obj).first()
    
    
    website_link.short_description = 'website'
    photo_img.short_description = 'foto'
    email.short_description = 'E-mail'
    phone.short_description = 'Telefone'


admin.site.register(Speaker, SpeakerAdmin)
admin.site.register(Talk)
admin.site.register(Course)
