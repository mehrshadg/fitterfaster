# Generated by Django 3.1.2 on 2020-10-28 00:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meals', '0010_auto_20201028_0009'),
    ]

    operations = [
        migrations.AddField(
            model_name='meal',
            name='meal_type',
            field=models.PositiveSmallIntegerField(choices=[(0, 'Breakfast'), (1, 'Lunch'), (2, 'Dinner'), (3, 'Low-carb Snack'), (4, 'High-carb Snack')], default=0),
            preserve_default=False,
        ),
    ]
