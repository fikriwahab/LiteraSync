from django.urls import path
from main.views import display_items

app_name = 'main'

urlpatterns = [
    path('', display_items, name='display_items'),
]
