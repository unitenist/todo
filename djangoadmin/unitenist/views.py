from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Todo
from .forms import ListForm
def index(request):
    if request.method == "POST":
        form = ListForm(request.POST or None)
        if form.is_valid:
            form.save()
            todo_list = Todo.objects.all()
            return render(request,"unitenist/index.html",{'todo_list':todo_list})
    else:
        todo_list = Todo.objects.all()
        return render(request,"unitenist/index.html",{'todo_list':todo_list})
def about(request):
    return render(request,"unitenist/about.html")

def create(request):
    if request.method == "POST":
        form = ListForm(request.POST or None)
        if form.is_valid:
            form.save()
            todo_list = Todo.objects.all()
            return render(request,"unitenist/create.html",{'todo_list':todo_list})
    else:
        todo_list = Todo.objects.all()
        return render(request,"unitenist/create.html",{'todo_list':todo_list})
def delete(request,Todo_id):
    todo = Todo.objects.get(pk=Todo_id)
    todo.delete()
    return redirect("index")
def yesfinished(request,Todo_id):
    todo = Todo.objects.get(pk=Todo_id)
    todo.finished = False
    todo.save()
    return redirect("index")

def nofinished(request,Todos_id):
    todo = Todo.objects.get(pk=Todo_id)
    todo.finished = True  
    todo.save()
    return redirect("index")