from django.contrib import admin

from . import models


class NoteAdmin(admin.ModelAdmin):
    list_display = ('id', 'content')
    empty_value_display = '-None-'


admin.site.register(models.Note, NoteAdmin)
