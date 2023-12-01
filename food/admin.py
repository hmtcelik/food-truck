from django.contrib import admin
from .models import Food


class FoodAdmin(admin.ModelAdmin):
    list_display = (
        "location_id",
        "facility_type",
        "address",
        "latitude",
        "longitude",
        "created_at",
        "updated_at",
        "is_active",
    )
    list_editable = ("is_active",)
    list_filter = ("is_active",)
    search_fields = (
        "location_id",
        "facility_type",
        "address",
        "latitude",
        "longitude",
        "applicant",
        "food_items",
    )


admin.site.register(Food, FoodAdmin)
