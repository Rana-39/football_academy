from django.shortcuts import render
from django.http import HttpResponse

def AppBar(request):
    template = loader.get_template('AppBar.html')
    return HttpResponse(template.render())