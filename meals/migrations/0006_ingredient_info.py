# Generated by Django 3.1.2 on 2020-10-27 23:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meals', '0005_auto_20201027_2337'),
    ]

    operations = [
        migrations.AddField(
            model_name='ingredient',
            name='info',
            field=models.CharField(blank=True, default=None, max_length=500, null=True),
        ),
    ]