from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.
class techView(TemplateView):
    template_name = "_tech_summit/tech_blog.html"
