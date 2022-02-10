from django.conf import settings
from django.db import models


class Mandapform(models.Model):
    "Generated Model"
    category = models.CharField(
        max_length=256,
    )
    type = models.CharField(
        max_length=256,
    )


class List(models.Model):
    "Generated Model"
    name = models.CharField(
        max_length=256,
    )
    address = models.CharField(
        max_length=256,
    )
    category = models.CharField(
        max_length=256,
    )
