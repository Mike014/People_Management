from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .models import People

@user_passes_test(lambda u: u.is_superuser)
def people_list(request):
    people = People.objects.all()
    return render(request, 'people/list.html', {'people': people})

@user_passes_test(lambda u: u.is_superuser)
def add_person(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        surname = request.POST.get('surname')
        person = People(name=name, surname=surname)
        person.save()
        return redirect('people_list')
    return render(request, 'people/add.html')

@user_passes_test(lambda u: u.is_superuser)
def remove_person(request, person_id):
    person = get_object_or_404(People, id=person_id)
    person.delete()
    return redirect('people_list')

def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('people_list')
        else:
            return render(request, 'registration/login.html', {'error': 'Invalid credentials'})
    return render(request, 'registration/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'




 
