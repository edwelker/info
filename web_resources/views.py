# Create your views here.
from django.shortcuts import render_to_response
from models import PrimaryResource

def home(request):  
    return render_to_response('home.html', {'resources': PrimaryResource.objects.all()})

def all(request):
    return render_to_response('resources.xml', {'resources': PrimaryResource.objects.all()}, mimetype='text/xml')

def id(request, id):
    return render_to_response('resources.xml', {'resources': PrimaryResource.objects.filter(pk=id)}, mimetype='text/xml')
