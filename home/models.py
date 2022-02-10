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
    vendorname = models.CharField(
        max_length=256,
        blank=True,
    )
    address = models.CharField(
        max_length=256,
        blank=True,
    )
    category = models.CharField(
        max_length=256,
        blank=True,
    )
    vendorcategory = models.OneToOneField(
        "home.Mandapform",
        null=True,
        blank=True,
        on_delete=models.PROTECT,
        related_name="list_vendorcategory",
    )
