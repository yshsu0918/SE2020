from django.db import models

# Create your models here.


class order_record(models.Model):
    order_time = models.CharField(primary_key=True, max_length = 200)
    item_id = models.CharField(null = True, max_length = 5000)
    amount = models.CharField(null = True, max_length = 100)
    price = models.CharField(null = True, max_length = 100)
    total = models.CharField(null = True, max_length = 100)
    valid = models.CharField(null = True, max_length = 5)