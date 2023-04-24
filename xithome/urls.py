from . import views
from django.urls import path
# from .views import techView

urlpatterns = [
    path("", views.home, name="home"),
    path("about", views.about, name="about"),
    path("contact", views.contact, name="contact"),
    # path("tech", techView.as_view(), name='tech'),
]
