# Generated by Django 3.2.16 on 2022-11-08 18:21

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('quote', '0008_quotedetails'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='QuoteDetails',
            new_name='QuoteData',
        ),
    ]