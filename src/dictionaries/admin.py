from django.contrib import admin

from .models import Word


class WordAdmin(admin.ModelAdmin):
    list_display = ('id', 'keyword', 'meaning', 'synonym', 'antonym')
    empty_value_display = '-None-'


admin.site.register(Word, WordAdmin)
