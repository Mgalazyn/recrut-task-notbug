from django.shortcuts import render

# Create your views here.


def login_user(request):
    context = {}
    return render(request, 'login.html', context)



def register_user(request):
    context = {}
    return render(request, 'register.html', context)