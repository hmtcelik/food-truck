from django.urls import path
from .views import IndexView, FoodListView, FoodDetailView

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("food/", FoodListView.as_view(), name="food_list"),
    path("food/<int:pk>/", FoodDetailView.as_view(), name="food_detail"),
]
