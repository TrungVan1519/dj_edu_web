from django.db import models


class Url(models.Model):
    uuid = models.CharField(max_length=10)
    link = models.CharField(max_length=255)

    def __str__(self):
        return f'Url({self.uuid}, {self.link})'
