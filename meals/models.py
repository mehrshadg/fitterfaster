from enum import Enum
from django.utils.translation import gettext_lazy as _
from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class MealType(models.IntegerChoices):
    BREAKFAST = 0, _("Breakfast")
    LUNCH = 1, _("Lunch")
    DINNER = 2, _("Dinner")
    SNACK_LOW_CARB = 3, _("Low-carb Snack")
    SNACK_HIGH_CARB = 4, _("High-carb Snack")


class Meal(models.Model):
    name = models.CharField(max_length=200)
    meal_type = models.PositiveSmallIntegerField(choices=MealType.choices)
    page = models.PositiveIntegerField()
    items = models.ManyToManyField(Item, related_name="meals", through="Ingredient")
    description = models.TextField(null=True, default=None, blank=True)
    notes = models.TextField(null=True, default=None, blank=True)

    def __str__(self):
        return self.name


class IngredientUnit(models.TextChoices):
    GRAMS = "g", _("Grams")
    TABLE_SPOON = "tbsp", _("Table spoon")
    TEA_SPOON = "tsp", _("Tea spoon")
    SMALL = "small", _("Small")
    MEDIUM = "medium", _("Medium")
    LARGE = "large", _("Large")
    SIZE = "size", _("Size")
    CLOVE = "clove", _("Clove")
    HANDFUL = "handful", _("Handful")
    SLICE = "slice", _("Slice")
    ML = "ml", _("Milliliter")


class Ingredient(models.Model):
    meal = models.ForeignKey(Meal, models.CASCADE)
    item = models.ForeignKey(Item, models.CASCADE)
    info = models.CharField(max_length=500, default=None, null=True, blank=True)
    amount_level1 = models.FloatField()
    amount_level2 = models.FloatField()
    amount_level3 = models.FloatField()
    amount_level4 = models.FloatField()
    amount_level5 = models.FloatField()
    amount_level6 = models.FloatField()
    unit = models.CharField(max_length=10, choices=IngredientUnit.choices)

    def __str__(self):
        return self.item.name


class Day(models.TextChoices):
    MONDAY = "mon", _("Monday")
    TUESDAY = "tue", _("Tuesday")
    WEDNESDAY = "wed", _("Wednesday")
    THURSDAY = "thu", _("Thursday")
    FRIDAY = "fri", _("Friday")
    SATURDAY = "sat", _("Saturday")
    SUNDAY = "sun", _("Sunday")


class Time(models.IntegerChoices):
    BREAKFAST = 0, _("Breakfast")
    LUNCH = 1, _("Lunch")
    DINNER = 2, _("Dinner")
    SNACK_MORNING = 3, _("Morning Snack")
    SNACK_EVENING = 4, _("Evening Snack")


class WeeklyPlan(models.Model):
    start_date = models.DateField(unique=True)

    def __str__(self):
        return f"Starting: {self.start_date}"


class DayTimeMeal(models.Model):
    plan = models.ForeignKey(WeeklyPlan, on_delete=models.CASCADE, related_name="meals")
    day = models.CharField(max_length=3, choices=Day.choices)
    time = models.PositiveSmallIntegerField(choices=Time.choices)
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE)
    calorie_level = models.SmallIntegerField(choices=[(i, i) for i in range(1, 7)])

    class Meta:
        unique_together = ("day", "time", "plan")

    def __str__(self):
        return f"{Day(self.day).label} {Time(self.time).label}"




