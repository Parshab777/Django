from django.shortcuts import render , HttpResponse

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
