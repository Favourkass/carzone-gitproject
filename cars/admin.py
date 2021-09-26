from django.contrib import admin
from django.utils.html import format_html
from .models import Car

class CarAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{url}" width="40" style = "border-radius: 50px;" />'.format(
            url=object.car_photo.url,
        )) 
    thumbnail.short_description = 'photo'
    list_display = ('id','thumbnail','car_title', 'model', 'year', 'price', 'color', 'city', 'is_featured')
    list_display_links = ('id', 'thumbnail', 'car_title')
    list_editable  = ('is_featured',)
    list_filter = ('body_style', 'model', 'color','city')
    search_fields = ('id', 'car_title', 'city', 'model', 'body_style', 'fuel_type')
    # list_per_page = 25
# Register your models here.
admin.site.register(Car, CarAdmin)