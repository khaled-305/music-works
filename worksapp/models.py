from django.db import models

class MusicWorks(models.Model):
    title = models.TextField(max_length=100, null=True, blank=True, unique=True, help_text='music work title')
    contributors = models.CharField(max_length=250, null=True, blank=True, unique=True, help_text='contributors of a music work')
    iswc = models.CharField(max_length=200, null=True, blank=True, unique=True, help_text='music work iswc')

    def __str__(self):
        return f'{self.title} {self.iswc}'
