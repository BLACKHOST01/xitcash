from .views import techView
from django.urls import path


urlpatterns = [
    path("", techView.as_view(), name='techhome')
]
