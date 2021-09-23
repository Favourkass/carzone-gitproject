from django.contrib import admin
from .models import Team
from django.utils.html import format_html
# Register your models here.

class TeamAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{url}" width="40" style = "border-radius: 50px;" />'.format(
            url=object.photo.url,
        )) 

    thumbnail.short_description = 'photo'
    list_display = ('id', 'thumbnail', 'firstname', 'designation', 'created_date')
    list_display_links = ('id', 'firstname')
    search_fields = ('firstname', 'lastname', 'designation')
    list_filter = ('designation',)

admin.site.register(Team, TeamAdmin) 

