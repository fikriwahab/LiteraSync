from django.shortcuts import render
from .models import Item
from django.http import HttpResponseRedirect, HttpResponse
from main.forms import ItemForm
from django.urls import reverse
from django.core import serializers
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages  
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
#Tugas 5 on bonus tugas 4
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Item
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone

#Bonus tugas 6
def delete_item_ajax(request, item_id):
    if request.method == "DELETE":
        try:
            item = Item.objects.get(id=item_id)
            item.delete()
            return JsonResponse({'status': 'success'}, status=200)
        except Item.DoesNotExist:
            return JsonResponse({'status': 'failed', 'message': 'Item not found'}, status=404)
    return JsonResponse({'status': 'failed', 'message': 'Invalid request method'}, status=400)

@csrf_exempt
@login_required(login_url='/login')
def add_item(request):
    if request.method == 'POST':
        # Menerima data dari POST request
        print(request.POST)
        item_name = request.POST.get('name')
        item_amount = request.POST.get('amount')
        item_description = request.POST.get('description')

        # Membuat objek baru dan menyimpannya
        new_item = Item(name=item_name, amount=item_amount, description=item_description, created_at=timezone.now(), user=request.user)
        new_item.save()

        return JsonResponse({'message': 'Item successfully added!'}, status=201)
    else:
        return JsonResponse({'error': 'Invalid method'}, status=400)

@login_required(login_url='/login')
def get_items_json(request):
    items = Item.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("json", items), content_type="application/json")
# Tugas 6

@login_required(login_url='/login')
def increment_item(request, item_id):
    try:
        item = Item.objects.get(id=item_id, user=request.user)
        item.amount += 1
        item.save()
        messages.success(request, 'Item added!')
    except Item.DoesNotExist:
        messages.error(request, 'Item does not exist!')
        return Http404("Item does not exist.")
    return HttpResponseRedirect(reverse('main:display_items'))

@login_required(login_url='/login')
def decrement_item(request, item_id):
    try:
        item = Item.objects.get(id=item_id, user=request.user)
        if item.amount > 0:
            item.amount -= 1
            item.save()
            messages.success(request, 'Item reduced!')
        else:
            messages.warning(request, 'Item amount is already 0.')
    except Item.DoesNotExist:
        messages.error(request, 'Item does not exist!')
        return Http404("Item does not exist.")
    return HttpResponseRedirect(reverse('main:display_items'))

@login_required(login_url='/login')
def delete_item(request, item_id):
    try:
        item = Item.objects.get(id=item_id, user=request.user)
        item.delete()
        messages.success(request, 'Item deleted!')
    except Item.DoesNotExist:
        messages.error(request, 'Item does not exist!')
        return Http404("Item does not exist.")
    return HttpResponseRedirect(reverse('main:display_items'))


def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # Check if username and password fields are empty
        if not username or not password:
            messages.error(request, 'Please provide both username and password.')
            return render(request, 'login.html')
        
        # Check if username exists
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            messages.error(request, 'Username does not exist.')
            return render(request, 'login.html')

        # Then, try to authenticate the user
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("main:display_items")) 
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.error(request, 'Password is incorrect.')
    context = {}
    return render(request, 'login.html', context)


def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

@login_required(login_url='/login')
def display_items(request):
    items = Item.objects.filter(user=request.user)
    total_items = items.count()
    return render(request, 'main.html', {'name': request.user.username,'items': items, 'total_items': total_items, 'last_login': request.COOKIES.get('last_login', 'Not available')})

    
def create_item(request):
    form = ItemForm(request.POST or None)
    print("Form is valid:", form.is_valid())
    print("Request method:", request.method)
    if form.is_valid() and request.method == "POST":
        item = form.save(commit=False)
        item.user = request.user
        item.save()
        return HttpResponseRedirect(reverse('main:display_items'))

    context = {'form': form}
    return render(request, "create_item.html", context)

def show_xml(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")