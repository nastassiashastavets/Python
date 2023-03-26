from django.shortcuts import render, get_object_or_404, redirect
from .forms import UserForm
from django.views.generic import TemplateView
from .models import TodoListItem
from django.http import HttpResponseRedirect, HttpResponse

def index(request):
    return HttpResponse("Добро пожаловать! Это мой дипломный проект!")
    userform = UserForm()
    return render(request, 'todolist.html',
        {'form': userform})

class HomePageView(TemplateView):
    template_name = 'home.html'

def todoappView(request):
    all_todo_items = TodoListItem.objects.all()
    return render(request, 'todolist.html',
        {'all_items': all_todo_items})

def addTodoView(request):
    x = request.POST['content']
    new_item = TodoListItem(content=x)
    new_item.save()
    return HttpResponseRedirect('/todoapp/')


def deleteTodoView(request, i):
    y = TodoListItem.objects.get(id=i)
    y.delete()
    return HttpResponseRedirect('/todoapp/')






