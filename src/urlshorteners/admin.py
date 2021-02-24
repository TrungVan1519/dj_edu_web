from django.contrib import admin

from .models import Url


class UrlAdmin(admin.ModelAdmin):
    list_display = ('id', 'uuid', 'link')
    empty_value_display = '-None-'


admin.site.register(Url, UrlAdmin)
