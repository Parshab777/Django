from django.shortcuts import render , HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("Hello World")



def contact(request):
    context = {
        'name':'Contact'
    }
    return render(request , 'home.html' , context)