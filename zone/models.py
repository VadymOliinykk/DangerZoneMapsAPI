from django.db import models

# Create your models here.
from user.models import User


class Zone(models.Model):
    name = models.CharField(default="Default name", max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    type_options = [
        ('NT', 'Natural'),
        ('TG', 'Technogenic'),
        ('AG', 'Anthropogenic'),
        ('EC', 'Ecological'),
    ]
    zone_type = models.CharField(choices=type_options, max_length=5)
    lat = models.FloatField(default=0)
    lon = models.FloatField(default=0)
    radius = models.IntegerField(default=0)
    description = models.TextField(default=" ", max_length=255)
    is_showing = models.BooleanField(default=False)

    def __str__(self):
        return self.name + ".By " + self.author.username


