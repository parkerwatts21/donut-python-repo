from django.db import models

# Create your models here.
class Doughnut(models.Model):
    name = models.CharField(max_length=255)  # Name of the doughnut
    price = models.DecimalField(max_digits=5, decimal_places=2)  # Price with up to 2 decimal places
    type = models.CharField(max_length=50)  # Type of doughnut (e.g., "cake", "glazed", etc.)

    class Meta:
        db_table = 'doughnuts'  # Database table name

    def __str__(self):
        return f"{self.name} (${self.price})"