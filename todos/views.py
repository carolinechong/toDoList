from django.shortcuts import render, redirect
from .models import Todo
from .forms import TodoForm
from django.contrib import messages

def index(request):
    if request.method == 'POST':
        form = TodoForm(request.POST or None)

        if form.is_valid():
            form.save()
            todos = Todo.objects.all
            messages.success(request, ('Item has been added to the list.'))
            return render(request, 'todos/index.html', {'todos': todos})

    else:
        todos = Todo.objects.all
        return render(request, 'todos/index.html', {'todos': todos})

def view(request, todo_id):
    context = {
        'todo': Todo.objects.get(id=todo_id),
    }
    return render(request, 'todos/view.html', context)

def delete(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.delete()
    messages.success(request, 'Item has been deleted.')
    return redirect('/')

def todo_pending(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.completed = False
    todo.save()
    return redirect('/')
    
def todo_completed(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.completed = True
    todo.save()
    return redirect('/')

def edit(request, todo_id):
    if request.method == 'POST':
        todos = Todo.objects.get(id=todo_id)

        form = TodoForm(request.POST or None, instance=todos)

        if form.is_valid():
            form.save()
            messages.success(request, ('Item has been edited.'))
            return redirect('/')

    else:
        todos = Todo.objects.get(id=todo_id)
        return render(request, 'todos/edit.html', {'todos': todos})
