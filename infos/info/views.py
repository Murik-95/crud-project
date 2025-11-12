from django.shortcuts import render, redirect, get_object_or_404
from .models import Person
from .forms import PersonForm

def index(request):
    error = ''
    pers = Person.objects.all()
    return render(request, 'info/index.html', {'pers': pers})


def create(request):
    error = ''
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Пишите данные корректно'
    form = PersonForm()

    return render(request, 'info/create.html', {'form': form, 'error': error})

def edit(request, pk):
    person = get_object_or_404(Person, pk=pk)
    error = ''
    if request.method == 'POST':
        form = PersonForm(request.POST, instance=person)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Пишите данные корректно'
    form = PersonForm(instance=person)

    return render(request, 'info/edit.html', {'form': form, 'error': error})

def delete(request, pk):
    person = get_object_or_404(Person, pk=pk)
    person.delete()
    return redirect('home')
