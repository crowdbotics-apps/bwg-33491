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
    vendoraddress = models.ForeignKey(
        "home.List",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="list_vendoraddress",
    )
    vendorcategory = models.ForeignKey(
        "home.Mandapform",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="list_vendorcategory",
    )
    vendorname = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="list_vendorname",
    )
