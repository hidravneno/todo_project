from django.shortcuts import render, redirect, get_object_or_404
from .models import Task  
from .forms import TaskForm 

def task_list(request):
    tasks = Task.objects.all()
    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    
    return render(request, 'task/task_list.html', {'tasks': tasks, 'form': form})  

def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id) 
    task.delete()
    return redirect('task_list')

def complete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.complete = True 
    task.save()
    return redirect('task_list')

def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'task/edit_task.html', {'form': form, 'task': task})

def task_detail(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    return render(request, 'task/task_detail.html', {'task': task})