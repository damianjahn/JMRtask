from django.db import models


# Create your models here.


class Urlshortcut(models.Model):
    address = models.CharField(max_length=500)  # CharField({'max_legth':500})
    shortcut = models.UUIDField()

    def __str__(self):
        return "{} - {}".format(self.shortcut, self.address)
