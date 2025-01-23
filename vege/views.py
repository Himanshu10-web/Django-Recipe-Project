from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import *

# Create your views here.
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


def delete_receipe(request, id):
    queryset = Recepie.objects.get(id = id)
    queryset.delete()
    return redirect('/receipes')

