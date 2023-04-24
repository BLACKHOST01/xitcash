from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from .models import article


# Create your views here.
def home(request):
     mo = article
     return render(request, "_home/index.html")

def cash(request):
     return render(request, cash.html)

def about(request):
     
     return render(request, "_home/about.html")

def contact(request):
     return render(request, "_home/contact.html")

def blog(request):
     pass
# class techView(ListView):
#     model = article
#     template_name = "_tech_summit/tech_home.html"
# class ModelView(TemplateView):
#     template_name = "_tech_summit/tech_home.html"

