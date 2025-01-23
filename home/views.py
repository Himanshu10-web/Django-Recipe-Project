from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def Index(request):
    peoples = [
        {'name' : 'Himanshu' , 'age' : 17},
        {'name' : 'Vicky' , 'age' : 30},
        {'name' : 'John' , 'age' : 32},
    ]


    vegetables = ['tomato', 'potato', 'pumpkin']
   

    return render(request, "index.html", context = {'page' : ' Django tutorial 2025', 'peoples' : peoples, 'vegetables' : vegetables})

def About_page(request):
    context = {'page' : 'About'}
    return render(request, "about.html", context)


def Contact_page(request):
    context = {'page' : 'Contact'}
    return render(request, "contact.html", context)