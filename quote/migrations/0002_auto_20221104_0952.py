# Generated by Django 3.2.16 on 2022-11-04 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quote', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quote',
            name='quote_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='quote',
            name='submitted_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]