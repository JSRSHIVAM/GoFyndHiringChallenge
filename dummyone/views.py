from django.shortcuts import render

# Create your views here.

# Create your views here.
from django.views.generic import TemplateView

class StaticView(TemplateView):
   template_name = "chart.html"