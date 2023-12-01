from django.db import models


class Food(models.Model):
    location_id = models.IntegerField()
    applicant = models.CharField(max_length=200)
    facility_type = models.CharField(max_length=200)
    location_description = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    food_items = models.CharField(max_length=200)
    latitude = models.FloatField()
    longitude = models.FloatField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.location_id} - {self.address[:10]}..."
