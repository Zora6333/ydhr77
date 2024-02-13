from django.db import models

class JSONData(models.Model):
    name = models.CharField(max_length=50)
    date = models.DateTimeField()

    def __str__(self):
        return self.name