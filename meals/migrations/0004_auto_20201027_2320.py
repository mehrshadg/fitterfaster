# Generated by Django 3.1.2 on 2020-10-27 23:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meals', '0003_auto_20201027_2318'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ingredient',
            old_name='amount',
            new_name='amount_level1',
        ),
        migrations.RemoveField(
            model_name='ingredient',
            name='calorie_level',
        ),
        migrations.AddField(
            model_name='ingredient',
            name='amount_level2',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ingredient',
            name='amount_level3',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ingredient',
            name='amount_level4',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ingredient',
            name='amount_level5',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ingredient',
            name='amount_level6',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]
