from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from ledger.models import Recipe
from django.contrib.auth.mixins import LoginRequiredMixin


class RecipeListView(ListView):
    model = Recipe
    template_name = "recipes_list.html"


class RecipeDetailView(DetailView, LoginRequiredMixin):
    model = Recipe
    template_name = "recipe_detail.html"
