from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=40)
    text = models.CharField(max_length=10000)
    uwords = models.IntegerField()

    def __str__(self):
        return self.title
