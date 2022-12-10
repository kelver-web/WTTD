from django.contrib import admin
from django.utils.html import format_html
from .models import Speaker, Contact, Talk

# Register your models here.


class ContactInLine(admin.TabularInline):
    model = Contact
    extra = 1

class SpeakerAdmin(admin.ModelAdmin):
    inlines = [ContactInLine]
    prepopulated_fields = {'slug': ('name',)}
    list_display = ['name', 'photo_img', 'website_link']

    def website_link(self, obj):
        return format_html('<a href="{0}" target="_blank">{0}</a>', obj.website)

    def photo_img(self, obj):
        return format_html('<img width="32px" src="{}"/>', obj.photo)
    
    website_link.short_description = 'website'
    photo_img.short_description = 'foto'


admin.site.register(Speaker, SpeakerAdmin)
admin.site.register(Talk)
