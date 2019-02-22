from django.shortcuts import render, redirect
#from django.http import HttpResponse
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
#restrict logged in users
from django.contrib.auth.decorators import login_required
from django.contrib import messages
#from django.contrib.auth.forms import UserCreationForm
from .forms import SignupForm, newTrip, editTrip
from django.contrib.auth.models import User
from django.db.models import Q

# Create your views here.

def index(request):
    msg = "Welcome! Let's Travel!"
    context = {'message': msg}
    if request.method == 'POST':
        print(request.POST)
        u = request.POST['email']
        p = request.POST['pwd']
        print(u,p)
        user = authenticate(username = u, password = p)
        print(user)
        if user is not None:
            if user.is_active:
                login(request, user)
                #return HttpResponseRedirect('dashboard.html')
                #return render(request, 'dashboard.html')
                return HttpResponseRedirect('dashboard')
        else:
            print('The username and password were incorrect.')
            #return render(request, 'index.html')
            return HttpResponseRedirect('/')
    else:
        return render(request, 'index.html', context)
        #return HttpResponseRedirect('/')

def signup(request):
    msg = "Welcome! Let's Travel!"
    context = {'message': msg}
    if request.method == 'POST':
        print(request.POST)
        fn = request.POST['first_name']
        ln = request.POST['last_name']
        u = request.POST['email']
        p = request.POST['pwd']
        p2 = request.POST['pwd_conf']
        print(fn,ln,u,p,p2)
        #user = authenticate(username = u, password = p)
        #print(user)
        r = User.objects.filter(username = u)
        if r.count():
            print("Email already exists")
            return HttpResponseRedirect('/')
        else:
            if p and p2 and p == p2:
                user = User.objects.create_user(first_name = fn, last_name = ln, username = u, password = p)
                login(request, user)
                return HttpResponseRedirect('dashboard')
            else:
                print('mismatch passwords')
                return HttpResponseRedirect('/')
    else:
        return render(request, 'index.html', context)
    return HttpResponseRedirect('/')

@login_required
def logout_view(request):
    msg = "We'll see you soon!"
    context = {'message': msg}
    logout(request)
    #return HttpResponseRedirect('')
    return render(request, 'logout.html', context)

@login_required
def dashboard(request):
    #print(user)
    username = request.user.first_name
    print(username)
    msg = 'Hello ' + username.title() + '!'
    #trips = Trip.objects.all()#filter(owner = user)
    #trips = [
    #    Trip(1, 'Nashville', '5/15/19', '6/5/19', 'Wrestlemania'),
    #    Trip(2, 'Paris', '10/15/19', '11/1/2019', 'cheese tour'),
    #    Trip(3, 'Buenos Aires', '11/3/19', '11/15/19', 'see Iguazy Falls'),
    #]
    trips = Trip.objects.filter(owner = request.user)
    trips3 = TripJoined.objects.filter(user = request.user)
    print('joined')
    print(trips3)
    #trips2
    trips3_nojoined = TripJoined.objects.all().exclude(user = request.user)
    #print('trips no joined')
    print(trips3_nojoined) 
    #trips2 = Trip.objects.filter( ~Q(owner = request.user) | ~Q(id = 8)   ) 
    trips2 = Trip.objects.exclude(id__in = trips3.values_list('trip')).exclude(owner = request.user)
    context = {'message': msg, 'trips': trips, 'trips_joined': trips3,'trips_others': trips2}
    #cap 2.2 create a class for each trip.
    return render(request, 'dashboard.html', context)

@login_required
def new(request):
    username = request.user.first_name
    msg = "Hello " + username.title() + "! Create a trip!"
    form = newTrip()
    context = {'message': msg, 'form': form }
    return render(request,'new.html', context)

@login_required
def post_trip(request):
    print('post create trip')
    form = newTrip(request.POST)
    if form.is_valid():
        trip = Trip(owner= request.user, 
            destination= form.cleaned_data['destination'], 
            plan= form.cleaned_data['plan'], 
            start_date = form.cleaned_data['start_date'], 
            end_date = form.cleaned_data['end_date']
        )
        trip.save()
    return HttpResponseRedirect('dashboard')

@login_required
def edit(request, id):
    print('edit trip')
    username = request.user.first_name
    print(id, username)
    my_trip = Trip.objects.get(id = id)
    print(my_trip.id)
    form = editTrip(instance = my_trip)
    msg = "Hello " + username.title() +"! Let's edit your trip!"
    context = {'message': msg, 'form': form, 'id': id}
    return render(request, 'edit.html', context)

@login_required
def post_edit(request, id):
    print('post edit')
    username = request.user.first_name
    #print(username, id)
    #my_trip = Trip.objects.get(id = id)
    #print(my_trip.id)
    form = editTrip(request.POST)#, instance = my_trip)
    if form.is_valid():
        trip = Trip.objects.get(id = id)
        trip.destination= form.cleaned_data['destination']
        trip.plan= form.cleaned_data['plan']
        trip.start_date = form.cleaned_data['start_date'] 
        trip.end_date = form.cleaned_data['end_date']
        trip.save()
    return redirect('dashboard')

@login_required
def remove(request, id):
    username = request.user.first_name
    print(id, username)
    my_trip = Trip.objects.get(id = id)
    my_trip.delete()
    #print(my_trip.id)
    #form = newTrip()
    #plan = 'nada concreto'
    #msg = "Hello " + username +"! Let's edit your trip!"
    #context = {'message': msg, 'form': form, 'plan': plan}
    return redirect('dashboard')

@login_required
def cancel(request, id):
    username = request.user.first_name
    print(id, username)
    my_trip = TripJoined.objects.get(id = id)
    my_trip.delete()
    #print(my_trip.id)
    #form = newTrip()
    #plan = 'nada concreto'
    #msg = "Hello " + username +"! Let's edit your trip!"
    #context = {'message': msg, 'form': form, 'plan': plan}
    return redirect('dashboard')

@login_required
def join(request, id):
    username = request.user.first_name
    print(id, username)
    trip = Trip.objects.get(id = id)
    join_trip = TripJoined(user = request.user, trip = trip )
    join_trip.save()
    #print(my_trip.id)
    #form = newTrip()
    #plan = 'nada concreto'
    #msg = "Hello " + username +"! Let's edit your trip!"
    #context = {'message': msg, 'form': form, 'plan': plan}
    return redirect('dashboard')

@login_required
def show(request, id):
    username = request.user.first_name
    msg = "Hello " + username.title() + "! Read about this trip!"
    trip = Trip.objects.get(id = id)
    trip_joined_people = TripJoined.objects.filter(trip = trip)
    context = {'message': msg, 'liga': 'show', 'trip': trip, 'people': trip_joined_people}
    return render(request, 'show.html', context)