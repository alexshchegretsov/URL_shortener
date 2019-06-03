from django.db import models

class Url(models.Model):
    long_url = models.URLField()
    short_url = models.URLField(blank=True)
    date_add = models.DateTimeField(auto_now_add=True)
    count = models.IntegerField(default=0)

    class Meta:
        ordering = ['-count']

    def __str__(self):
        return f'{self.long_url} | {self.count}'
