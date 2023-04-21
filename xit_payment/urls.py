from . import views
from django.urls import path

urlpatterns = [
    path("", views._payments, name="payments"),
]
