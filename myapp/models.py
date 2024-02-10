from django.db import models

# Create your models here.


class Music(models.Model):

    class Meta:

        db_table = 'movielist'

    title = models.CharField(max_length=200)
    seconds = models.IntegerField()

    def __str__(self):
        return self.title