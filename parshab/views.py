from django.shortcuts import render , HttpResponse , redirect
from .models import *
# Create your views here.
def homee(request):
    return render(request,'home.html')


def about(request):
    return HttpResponse("From About!!!!")

def contact(request):
    person = [
        {
            'name':'ram',
            'age':'35',
        },
        {
            'name':'parshab',
            'age':'15',
        },
        {
            'name':'Shyam',
            'age':'60',
        },
        {
            'name':'hari',
            'age':'35',
        },
    ]
    context = {
        'name': 'Contact Page',
        'Persons': person
    }
    return render(request,'contact.html',context)


def task(request):
    task = Todolist.objects.all()
    context = {
        'tasks': task
    }
    return render(request,'task.html',context)


def form(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        if title == '' or description == '':
            context = {
                'error':'Please fill both Fields.'
            }
            return render(request,'form.html',context)
        else:
            Todolist.objects.create(title = title,description=description)
            return redirect('form/')
    return render(request,'form.html')


def mark(request,pk):
    task = Todolist.objects.get(pk = pk)
    task.is_completed = False
    task.save()
    return redirect('/')

def edit_task(request,pk):
    task = Todolist.objects.get(pk=pk)
    context = {
        "tasks":task
    }
    if request.method == 'POST':
        # getting the data from the form
        titles = request.POST.get('title')
        descriptions = request.POST.get('description')
        if titles == '' or descriptions == '':
            context = {
                'error':'Please fill both Fields.'
            }
            return render(request,'edit.html',context)
            # Now editing the task
        task.title = titles
        task.description = descriptions
        task.save()
        return redirect("task/")
    return render(request,'edit.html',context)
    
def delete_task(request,pk):
    task = Todolist.objects.get(pk = pk)
    context = {'tasks':task}
    if request.method == 'POST':
        task.delete()
        return redirect('/')
    return render(request,'delete.html',context)

    
