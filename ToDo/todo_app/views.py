from django.shortcuts import get_object_or_404, render, redirect
from .models import todomodel

def index(request):
    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")

        new_todo = todomodel(title=title, description=description)
        new_todo.save()
        return redirect('index')  # Redirect to the same page index.html

    todos = todomodel.objects.all()
    context = {'todos': todos}
    return render(request, "todo_app/index.html", context)


def delete_todo(request, id):
    if request.method == 'POST':
        todo = todomodel.objects.get(id=id)
        todo.delete()
    return redirect('index')

def update_todo(request, id):
    todo=todomodel.objects.get(id=id)
    if request.method == 'POST':
        title=request.POST.get("title")
        description=request.POST.get("description")
        checked=request.POST.get("completed")=="on"

        todo.title=title
        todo.description=description
        todo.completed=checked
        todo.save()
        return redirect("index")

    context={'todo':todo}
    return render(request, "todo_app/update.html", context)


def complete_todo(request, id):
    todo=todomodel.objects.get(id=id)
    if request.method=='POST':
        todo.completed= not todo.completed
        todo.save()
    return redirect("index")
