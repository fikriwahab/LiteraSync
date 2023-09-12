from django.shortcuts import render
from .models import Item

def display_items(request):
    items = Item.objects.all()
    return render(request, 'main.html', {'items': items})
