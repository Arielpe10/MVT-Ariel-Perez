from django.shortcuts import render

from Mi_MVT.Familia.models import Familiar

# Create your views here.

def home(request):
    return render(request,'home.html',context={})

def crear_familiar(request):
    familiar = Familiar.objects.create(nombre = "Ariel", apellido = "Perez", nacimiento = "26-12-1996", edad = 25)
    context = {"familiar": familiar}
    return render (request, "home.html", context)

def ver_familiares(request):
    familiares = Familiar.objects.all()
    context = {"familiar": familiares}
    return render (request, "home.html", context)