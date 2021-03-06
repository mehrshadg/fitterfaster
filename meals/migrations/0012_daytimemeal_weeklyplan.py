# Generated by Django 3.1.2 on 2020-10-28 00:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('meals', '0011_meal_meal_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='WeeklyPlan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='DayTimeMeal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(choices=[('mon', 'Monday'), ('tue', 'Tuesday'), ('wed', 'Wednesday'), ('thu', 'Thursday'), ('fri', 'Friday'), ('sat', 'Saturday'), ('sun', 'Sunday')], max_length=3)),
                ('time', models.PositiveSmallIntegerField(choices=[(0, 'Breakfast'), (1, 'Lunch'), (2, 'Dinner'), (3, 'Morning Snack'), (4, 'Evening Snack')])),
                ('meal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='meals.meal')),
                ('plan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='meals', to='meals.weeklyplan')),
            ],
            options={
                'unique_together': {('day', 'time', 'plan')},
            },
        ),
    ]
