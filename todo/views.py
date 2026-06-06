from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def task_list(request):
    return render(request, 'task_list.html')

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
