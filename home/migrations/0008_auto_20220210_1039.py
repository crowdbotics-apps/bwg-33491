# Generated by Django 2.2.26 on 2022-02-10 10:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_auto_20220210_1037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='list',
            name='vendoraddress',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='list_vendoraddress', to=settings.AUTH_USER_MODEL),
        ),
    ]
