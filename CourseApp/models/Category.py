from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        db_table = 'category'
