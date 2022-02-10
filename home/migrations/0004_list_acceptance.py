# Generated by Django 2.2.26 on 2022-02-10 10:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_list'),
    ]

    operations = [
        migrations.AddField(
            model_name='list',
            name='acceptance',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='list_acceptance', to='home.Mandapform'),
        ),
    ]