from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.template import RequestContext
from datetime import datetime
from django.core.serializers import serialize
from geoQuakesApp.models import Quake
from django.template.context import Context
import pandas as pd

# Create your views here.
def quake_dataset(request):
    quakes = serialize('json', Quake.objects.order_by("ID")[:500])
    return HttpResponse(quakes, content_type='json')

def home_view(request):
    return render(
        request, 
        'app/index.html',
        {
            'title': 'Home Page'
        }
    )