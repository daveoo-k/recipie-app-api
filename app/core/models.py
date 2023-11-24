from django.db import models # noqa


class Ingredient(models.Model):
    """Ingredient for recipies."""
    name = ()