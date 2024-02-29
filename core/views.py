from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Member

def hello(request):
    return HttpResponse('hello world')

def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())

def index(request):
    users = Member.objects.all().values()
    template = loader.get_template('index.html')
    context = {
        'users': users,
    } 
    return HttpResponse(template.render(context, request))

def details(request, id):
    users = Member.objects.get(id=id)
    template = loader.get_template('details.html')
    context = {
        'users': users,
    }
    return HttpResponse(template.render(context, request))

def testing(request):
  template = loader.get_template('template.html')
  context = {
    'fruits': ['Apple', 'Banana', 'Cherry'],   
  }
  return HttpResponse(template.render(context, request))



