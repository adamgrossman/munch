from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from dish_server.forms import EmailUserCreationForm, ClubForm, RestaurantForm
from dish_server.models import Member, Club, Restaurant


# HOME, PROFILE, AND REGISTRATION
def home(request):
    return render(request, 'home.html')


def register(request):
    if request.method == 'POST':
        form = EmailUserCreationForm(request.POST)
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
    data = {'member': member}
    return render(request, "clubs.html", data)


def all_clubs(request, club_id):
    club = Club.objects.get(pk=club_id)
    data = {'club': club}
    return render(request, "profile.html", "clubs.html", data)


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
    members = {}
    for member in Member.objects.all():
        group_id = member.clubs.values('id')
        restaurants = Restaurant.objects.filter(group__pk__in=group_id).distinct()
        members[member.clubs] = restaurants

    food = Restaurant.objects.all()
    data = {"members": members, 'food': food}
    return render(request, 'restaurant.html', data)

#
# def all_restaurants(request):
#
#
#
#     # user_clubs = {}
#     # for club in request.user.id():
#     #     club_ids = club.restaurants.values('id')
#     #     clubs[club.restaurants] = club_ids
#
#     data = {}
#     return render(request, "restaurant.html", data)


#
# def all_restaurants(request, club_id):
#     member = Member.objects.get(pk=request.user.id)
#     club = Club.objects.get(pk=club_id)
#     restaurant = restaurants.clubs.get()
#     data = {"club": club}
#     return render(request, 'restaurant.html', data)


def dishes(request):
    return render(request, 'dishes.html')




# def view_club(request, club_id):
#     club = Club.objects.get(pk=club_id)
#     data = {'club': club}
#     return render(request, "clubs.html", data)


@login_required
def add_dish(request):

    if request.method == "POST":
        form = ClubForm(request.POST)
        if form.is_valid():
            if form.save():
                return redirect('dishes')
    else:
        form = ClubForm()
    data = {"form": form}

    return render(request, "add_dish.html", data)





# def upload_picture(request, member_id):
#     if request.method == 'POST':
#         picture_form = PictureForm(request.POST, request.FILES)
#         if picture_form.is_valid():
#             pic = Picture(description=picture_form.cleaned_data['description'],
#                           image=picture_form.cleaned_data['picture'],
#                           location=Member.objects.get(pk=member_id))
#             pic.save()
#         return redirect('view_location', member_id)