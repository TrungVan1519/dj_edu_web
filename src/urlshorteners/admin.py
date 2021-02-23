from django.contrib import admin

from . import models


class UrlAdmin(admin.ModelAdmin):
    list_display = ('id', 'uuid', 'link')
    empty_value_display = '-None-'


admin.site.register(models.Url, UrlAdmin)
