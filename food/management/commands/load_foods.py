from django.core.management.base import BaseCommand
from food.models import Food
from django.db import transaction
import pandas as pd


class Command(BaseCommand):
    def handle(self, **options):
        df = pd.read_csv("./utils/data/food-truck-data.csv").head(1000)

        with transaction.atomic():
            for _, row in df.iterrows():
                food = Food(
                    location_id=row["locationid"],
                    applicant=row["Applicant"],
                    facility_type=row["FacilityType"],
                    location_description=row["LocationDescription"],
                    address=row["Address"],
                    food_items=row["FoodItems"],
                    latitude=row["Latitude"],
                    longitude=row["Longitude"],
                )
                food.save()

        print("Foods loaded successfully")
