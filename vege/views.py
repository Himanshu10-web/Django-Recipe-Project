from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required



# Create your views here. 
@login_required(login_url = '/login/')
def receipes(request):
    if request.method == 'POST':
        data = request.POST
        receipe_image = request.FILES.get('receipe_image')
        receipe_name = data.get('receipe_name')
        receipe_description = data.get('receipe_description')
        
        Recepie.objects.create(
            receipe_name = receipe_name,
            receipe_description = receipe_description,
            receipe_image = receipe_image,
            )
        return redirect('/receipes')

    
    queryset = Recepie.objects.all()

    if request.GET.get('search'):
        queryset = queryset.filter(receipe_name__icontains = request.GET.get('search'))  #icontains give you any letter realted to the search you have entered 

    context = {'receipes' : queryset}
    return render(request, "receipes.html", context)

@login_required(login_url = '/login/')
def update_receipe(request, id):
    queryset = Recepie.objects.get(id = id)
    
    if request.method == "POST":
        data = request.POST
        receipe_image = request.FILES.get('receipe_image')
        receipe_name = data.get('receipe_name')
        receipe_description = data.get('receipe_description')

        queryset.receipe_name = receipe_name
        queryset.receipe_description = receipe_description
    
        if receipe_image:
            queryset.receipe_image = receipe_image

        queryset.save()
        return redirect('/receipes')
    
    

    context = {'receipe' : queryset}
    return render(request, 'update_receipe.html', context)

@login_required(login_url = '/login/')
def delete_receipe(request, id):
    queryset = Recepie.objects.get(id = id)
    queryset.delete()
    return redirect('/receipes')


def login_user(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not User.objects.filter(username = username).exists():

            messages.error(request, 'Invalid Username')
            return redirect('/login_user')
        
        user = authenticate(username = username , password = password)
        if user is None:
            messages.error(request, 'Invalid Password')
            return redirect('/login_user')
        
        else:
            login(request, user)
            return redirect('/receipes')

    return render(request, 'login_user.html')

def logout_user(request):
    logout(request)
    return redirect('/login_user')


def register_user(request):

    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')

        users = User.objects.filter(username = username)

        if users.exists():
            messages.info(request, 'Username already taken')
            return redirect('/register_user')
        

        user = User.objects.create(
            first_name = first_name,
            last_name = last_name,
            username = username 
        )

        
        
        user.set_password(password)
        user.save()
        messages.info(request, 'Account created successfully !!')

        return redirect('/register_user/')
    return render(request, 'register_user.html')