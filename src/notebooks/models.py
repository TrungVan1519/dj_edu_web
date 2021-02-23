from django.db import models


class Note(models.Model):
    content = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'Note({self.content})'
