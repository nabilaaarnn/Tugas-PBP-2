import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from todolist.models import todolistItem
from todolist.forms import taskform
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseNotFound
from django.core import serializers

@login_required(login_url='/todolist/login/')
def show_todolist(request):
    data_todolist = todolistItem.objects.all().filter(user=request.user)
    context = {
    'list_data': data_todolist,
    'nama': 'Rizka Nisrina Nabila',
    'npm': '2106653344',
    }
    return render(request, "todolist.html", context)

@login_required(login_url='/todolist/login/')
def show_todolist_ajax(request):
    context = {
        'nama': 'Rizka Nisrina Nabila',
        'npm': '2106653344',
    }
    return render(request, "todolist_ajax.html", context)

@login_required(login_url='/todolist/login/')
def submit_ajax(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        
        new_data = todolistItem(user=request.user, title=title, description=description, date=datetime.datetime.now())
        new_data.save()
        return HttpResponse(b"CREATED", status=201)
    return HttpResponseNotFound()

def show_json(request):
    data = todolistItem.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("json", data))

def show_json_by_id(request, id):
    data = BarangWishlist.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login')
    
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("todolist:show_todolist"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('todolist:login'))
    response.delete_cookie('last_login')
    return response

def create_task(request):
    if request.method == "POST":
        form = taskform(request.POST)
        form.instance.user = request.user
        form.instance.date = datetime.datetime.now()
        if form.is_valid():
            form.save()
            response = HttpResponseRedirect(reverse("todolist:show_todolist"))
            return response
    else:
        form = taskform()

    context = {'form':form}
    return render(request, 'createtask.html', context)

def delete(request, id):
    data = todolistItem.objects.get(id=id)
    data.delete()
    return redirect('todolist:show_todolist')

def done(request, id):
    data = todolistItem.objects.get(id=id)
    if data.done == False:
        data.done = True
    else:
        data.done = False
    data.save()
    return redirect('todolist:show_todolist')
