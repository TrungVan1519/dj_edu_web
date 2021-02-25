from django.contrib import admin

from .models import Question, Choice

admin.site.site_header = 'Polls Admin'
admin.site.site_title = 'Polls Admin Area'
admin.site.index_title = 'Welcome to the Polls Admin Area'


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'pub_date')
    fieldsets = (
        (None, {'fields': ['question_text']}),
        ('Date info', {'fields': ['pub_date'], 'classes': ('collapse')})
    )
    inlines = [ChoiceInline]


class ChoiceAdmin(admin.ModelAdmin):
    list_display = ('question', 'choice_text', 'votes')


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice, ChoiceAdmin)
