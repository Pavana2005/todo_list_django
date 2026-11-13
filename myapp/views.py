
from django.shortcuts import render, redirect, get_object_or_404
from .models import Task


# CREATE AND READ

def task(request):

    if request.method == "POST":
        title = request.POST.get('title')

        if title:
            Task.objects.create(title=title)

        return redirect('task')

    status = request.GET.get('status', 'all')

    tasks = Task.objects.all().order_by('-created_at')

    total = Task.objects.count()
    completed_count = Task.objects.filter(completed=True).count()
    active_count = Task.objects.filter(completed=False).count()

    if status == 'active':
        tasks = tasks.filter(completed=False)

    elif status == 'completed':
        tasks = tasks.filter(completed=True)

    return render(request, 'index.html', {
        'tasks': tasks,
        'total': total,
        'completed_count': completed_count,
        'active_count': active_count,
        'status': status
    })


# UPDATE

def update(request, id):

    t = get_object_or_404(Task, id=id)

    if request.method == "POST":
        t.title = request.POST.get('title')
        t.save()

        return redirect('task')

    return render(request, 'update.html', {'task': t})


# DELETE

def delete(request, id):

    t = get_object_or_404(Task, id=id)

    if request.method == "POST":
        t.delete()

    return redirect('task')


# COMPLETE

def complete(request, id):

    t = get_object_or_404(Task, id=id)

    if request.method == "POST":
        t.completed = not t.completed
        t.save()

    return redirect('task')
