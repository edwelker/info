# Create your views here.
from django.shortcuts import render_to_response
from models import Resource

def home(request):  
    return render_to_response('home.html', {'resources': Resource.objects.all()})

def all(request):
    return render_to_response('resources.xml', {'resources': Resource.objects.all()}, mimetype='text/xml')

def id(request, id):
    return render_to_response('resources.xml', {'resources': Resource.objects.filter(pk=id)}, mimetype='text/xml')
