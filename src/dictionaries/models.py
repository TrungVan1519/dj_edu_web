from django.db import models


class Word(models.Model):
    keyword = models.CharField(max_length=255)
    meaning = models.TextField()
    synonym = models.TextField(null=True, blank=True)
    antonym = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'Word({self.keyword}, {self.meaning}, {self.synonym}, {self.antonym})'
