from django.db import models
from django.conf import settings
# Create your models here.

class Recipe(models.Model):
    DFT = 'Draft'
    APR = 'Approved'
    PUB = 'Published'

    PHASES = [
        (DFT, 'Draft'),
        (APR, 'Approved'),
        (PUB, 'Published'),
    ]

    Breakfast = 'Breakfast'
    Lunch = 'Lunch'
    Dinner = 'Dinner'
    Dessert = 'Dessert'

    TYPES = [
        (Breakfast, 'Breakfast'),
        (Lunch, 'Lunch'),
        (Dinner, 'Dinner'),
        (Dessert, 'Dessert'),
    ]

    F = 'Fahrenheit'
    C = 'Celsius'

    DEGREE = [
        (F, 'Fahrenheit'),
        (C, 'Celsius'),
    ]

    image = models.ImageField(upload_to = 'recipes/', null = True)
    title = models.CharField(max_length = 150, null = True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE, null = True)
    published = models.CharField(
    max_length = 20,
    choices = PHASES,
    default = DFT,
    )
    meal_type = models.CharField(
        max_length = 15,
        choices = TYPES,
        default = Breakfast,
    )
    prep_time = models.IntegerField(null = True)
    cook_time = models.IntegerField(null = True)
    cook_temp = models.IntegerField(null = True)
    degree = models.CharField(
        max_length = 10,
        choices = DEGREE,
        default = F,
    )
    yeilds = models.IntegerField(null = True)
    food_type = models.CharField(
        max_length = 50,
        null = True,
        )
    ingredients = models.JSONField(
        encoder = None,
        decoder = None,
        null = True,
    )
    directions = models.CharField(
        max_length = 600,
        null = True,
    )
    notes = models.CharField(max_length = 250)

def __str__(self):
    return self.title[:100]
