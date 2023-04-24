from django.contrib import admin
from .models import user, article

# Register your models here.
admin.site.register(user)
admin.site.register(article)