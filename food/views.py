from django.shortcuts import render
from django.views import generic
from .models import Food


class IndexView(generic.TemplateView):
    template_name = "index.html"


# list view food
class FoodListView(generic.ListView):
    model = Food
    template_name = "food_list.html"
    context_object_name = "foods"

    def get_queryset(self):
        return Food.objects.all()[:9]


class FoodDetailView(generic.DetailView):
    model = Food
    template_name = "food_detail.html"
    context_object_name = "food"
