from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponseRedirect
from .models import TodoItem

def todoView(request):
    all_todo_items = TodoItem.objects.all()
    return render(request, 'todo.html',
        {'all_items':all_todo_items})

def addTodo(request):
    new_item = TodoItem(content = request.POST['content'])
    new_item.save()
    return  HttpResponseRedirect('/todo/')

def deleteTodo(request, startup_id):
    item_delete = TodoItem.objects.get(id=startup_id)
    item_delete.delete()
    return  HttpResponseRedirect('/todo/')