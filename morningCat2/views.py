from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegistrationForm

def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def gallery(request):
    return render(request, 'gallery.html')

def gallery_single(request):
    return render(request, 'gallery-single.html')

def services(request):
    return render(request, 'services.html')

def sample_inner_page(request):
    return render(request, 'sample-inner-page.html')

def contact(request):
    return render(request, 'contact.html')

def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created successfully")
            return redirect('my-register')
        else:
            messages.success(request, "Account creation failed")
            return redirect('my-register')
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})













