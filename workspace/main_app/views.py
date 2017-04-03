from django.shortcuts import render
from django.http import HttpResponse
import time
from .models import PageCount

# Create your views here.
def index(request):
    row, create = PageCount.objects.get_or_create(page='index')
    row.count = row.count + 1
    row.save()
    return HttpResponse('<h1>Hello World!</h1><br />The time is ' + time.strftime("%c") + '<br />You are visitor #' + str(row.count))
