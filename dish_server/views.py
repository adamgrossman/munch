from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from dish_server.forms import EmailUserCreationForm, ClubForm, RestaurantForm, DishForm
from dish_server.models import Member, Club, Restaurant, Dish


# HOME, PROFILE, AND REGISTRATION
def home(request):
    return render(request, 'home.html')


def register(request):
    if request.method == 'POST':
        form = EmailUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            if form.save():
                return redirect('login')
    else:
        form = EmailUserCreationForm()
    data = {'form': form}
    return render(request, 'registration/register.html', data)


@login_required
def profile(request):
    if not request.user.is_authenticated():
        return redirect('login')
    member = Member.objects.get(pk=request.user.id)
    data = {'member': member}
    return render(request, "profile.html", data)


# CLUBS
@login_required
def add_club(request):

    if request.method == "POST":
        form = ClubForm(request.POST)
        if form.is_valid():
            if form.save():
                return redirect('clubs')
    else:
        form = ClubForm()
    data = {"form": form}

    return render(request, "add_club.html", data)


def clubs(request):
    member = Member.objects.get(pk=request.user.id)
    members = Club.objects.filter(member=request.user)
    data = {'member': member, "members": members}
    return render(request, "clubs.html", data)


def view_club(request, club_id):
    clubs = Club.objects.get(pk=club_id)
    members = Club.objects.filter(member=request.user)
    data = {"clubs": clubs, "members": members}
    return render(request, "view_club.html", data)


# RESTAURANTS
@login_required
def add_restaurant(request):

    if request.method == "POST":
        form = RestaurantForm(request.POST)
        if form.is_valid():
            if form.save():
                return redirect('restaurants')
    else:
        form = RestaurantForm()
    data = {"form": form}

    return render(request, "add_restaurant.html", data)


def restaurants(request):
    restaurant = Restaurant.objects.all()

    data = {'restaurant': restaurant}
    return render(request, 'restaurant.html', data)


def view_restaurant(request, restaurant_id):
    view_restaurants = Restaurant.objects.get(pk=restaurant_id)
    data = {"view_restaurants": view_restaurants}
    return render(request, "view_restaurant.html", data)


# DISHES
@login_required
def add_dish(request):

    if request.method == "POST":
        form = DishForm(request.POST, request.FILES)
        if form.is_valid():
            if form.save():
                return redirect('dishes')
    else:
        form = DishForm()
    data = {"form": form}

    return render(request, "add_dish.html", data)


def dishes(request):
    munchies = Dish.objects.all()
    data = {"munchies": munchies}
    return render(request, 'dishes.html', data)


def view_dish(request, dish_id):
    dish = Dish.objects.get(pk=dish_id)
    data = {"dish": dish}
    return render(request, "view_dish.html", data)


# HUNGRY
def hungry(request):
    food = Dish.objects.order_by('?')[:1]
    food = food[0]
    data = {"food": food}
    return render(request, 'hungry.html', data)
