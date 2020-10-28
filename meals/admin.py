import csv

from django.contrib import admin
from django.contrib.admin import register
from django.http import HttpResponse
from django.urls import reverse
from django.utils.html import format_html

from meals import models


@register(models.Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ("name", )
    search_fields = ("name", )
    sortable_by = ("name", )


class IngredientInline(admin.TabularInline):
    model = models.Meal.items.through
    extra = 0
    autocomplete_fields = ("item", )


@register(models.Meal)
class MealAdmin(admin.ModelAdmin):
    list_display = ("name", "meal_type", "page")
    list_filter = ("meal_type", )
    search_fields = ("name", "page")
    sortable_by = ("name", "page")
    inlines = (IngredientInline, )


class DayTimeMealInline(admin.TabularInline):
    model = models.DayTimeMeal
    extra = 0
    autocomplete_fields = ("meal", )


@register(models.WeeklyPlan)
class WeeklyPlanAdmin(admin.ModelAdmin):
    list_display = ("start_date",)
    inlines = (DayTimeMealInline, )
    actions = ("grocery_list",)

    def grocery_list(self, request, queryset):
        plans = queryset.all()
        response = HttpResponse(content_type='text/csv')
        if len(plans) == 0:
            return response
        if len(plans) == 1:
            name = f"grocery_list_{plans[0]}.csv"
        else:
            name = "grocery_list.csv"
        response['Content-Disposition'] = f'attachment; filename={name}'
        writer = csv.writer(response)
        writer.writerow(["Item", "Info", "amount", "unit"])
        for obj in plans:
            for day_time_meal in obj.meals.all():
                amount_col_name = f"amount_level{day_time_meal.calorie_level}"
                for ing in day_time_meal.meal.ingredient_set.all():
                    writer.writerow([ing.item.name,
                                     ing.info,
                                     getattr(ing, amount_col_name),
                                     models.IngredientUnit(ing.unit).label])

        return response
    grocery_list.short_description = "Grocery List"





