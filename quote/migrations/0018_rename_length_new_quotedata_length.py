# Generated by Django 3.2.16 on 2022-11-09 10:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quote', '0017_remove_quotedata_length'),
    ]

    operations = [
        migrations.RenameField(
            model_name='quotedata',
            old_name='length_new',
            new_name='length',
        ),
    ]