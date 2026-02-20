from django.shortcuts import render,redirect
from .models import User
from .form import UserCreationForm
from django.contrib.auth import login
# Create your views here.

def registerUser(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employeelist')
    else:
        form = UserCreationForm()
    return render(request, 'core/register.html', {'form': form})