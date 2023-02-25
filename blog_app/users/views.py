from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm  
# Create your views here.
from .forms import EntriesForm
from .models import Profile, Entries
from django.http import Http404


def login_user(request):

    if request.user.is_authenticated:
        return redirect('main')
    
    if request.method == 'POST':
        username = request.POST['username'].lower()
        password = request.POST['password']

        user = User.objects.get(username=username)

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect(request.GET['next'] if 'next' in request.GET else 'main')

    return render(request, 'login.html')


def logout_user(request):
    logout(request)
    return redirect('login')


def register_user(request):
    form = UserCreationForm

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            
            login(request, user)
            return redirect('main')
        
    context = {'form': form}
    return render(request, 'register.html', context)


def main(request):
    entries = Entries.objects.all()
    print(entries)
    return render(request, 'main.html', {'entries': entries})


def add_entry(request):
    entry_owner = request.user.profile
    form = EntriesForm

    if request.method == 'POST':
        form = EntriesForm(request.POST, request.FILES)

        if form.is_valid():
            entry = form.save(commit=False)
            entry.owner = entry_owner
            entry.save()

            return redirect('main')

    contex = {'form': form}
    return render(request, 'entry_form.html', contex)


def view_entry(request, pk):

    try:
        entry = Entries.objects.get(id=pk)
    except Entries.DoesNotExist:
        raise Http404('Entry does not exist')
    
    context = {'entry': entry}
    return render(request, 'entry.html', context)
