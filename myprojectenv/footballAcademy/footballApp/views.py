# from django.shortcuts import render
# from django.http import HttpResponse

# def footballApp(request):
#     return HttpResponse("Hello world!")

from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def footballApp(request):
    template = loader.get_template('AppBar.html')
    return HttpResponse(template.render())