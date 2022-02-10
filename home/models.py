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
    vendorname = models.OneToOneField(
        "home.List",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="list_vendorname",
    )
    vendoraddress = models.ForeignKey(
        "home.List",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="list_vendoraddress",
    )
    vendorcategory = models.ForeignKey(
        "home.Mandapform",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="list_vendorcategory",
    )
