from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from .models import Task
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def task_list(request):
    tasks = Task.objects.filter(user=request.user)
    return render(request, 'task_list.html',{'tasks':tasks})

@login_required
def add_task(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        due_date = request.POST.get('due_date')
        Task.objects.create(
            user =request.user,
            title = title,
            due_date = due_date,
        )

        return redirect('task_list')
    return render(request, 'add_task.html')

@login_required
def update_task(request,id):
    task = Task.objects.get(id=id)
    if request.method == 'POST':
        task.title = request.POST.get('title')
        task.due_date = request.POST.get('due_date')
        task.completed = request.POST.get('completed') =='on'
        task.save()
        return redirect('task_list')
    return render(request,'update_task.html',{'task':task})

@login_required
def delete_task(request,id):
    task = Task.objects.get(id=id)
    task.delete()
    return redirect('task_list')




def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            print("USER CREATED:", user)  # DEBUG LINE
            return redirect('login')
        else:
            print("FORM ERRORS:", form.errors)  # DEBUG LINE

    else:
        form = UserCreationForm()

    return render(request, 'register.html', {'form': form})

