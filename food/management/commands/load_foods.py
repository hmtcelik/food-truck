from django.core.management.base import BaseCommand
from food.models import Food
from django.db import transaction
import pandas as pd


class Command(BaseCommand):
    def handle(self, **options):
        df = pd.read_csv("./utils/data/food-truck-data.csv").first(1000)

        with transaction.atomic():
            for _, row in df.iterrows():
                food = Food(
                    location_id=row["location_id"],
                    applicant=row["applicant"],
                    facility_type=row["facility_type"],
                    location_description=row["location_description"],
                    address=row["address"],
                    food_items=row["food_items"],
                    latitude=row["latitude"],
                    longitude=row["longitude"],
                )
                food.save()

        print("Foods loaded successfully")
