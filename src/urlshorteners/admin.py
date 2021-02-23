from django.contrib import admin

from . import models


class UrlAdmin(admin.ModelAdmin):
    list_display = ('uuid', 'link')


admin.site.register(models.Url, UrlAdmin)
