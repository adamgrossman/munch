from django import forms
from django.contrib.auth.forms import UserCreationForm
from dish_server.models import Member, Club, Dish, Restaurant


class EmailUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    city = forms.CharField()
    country = forms.CharField()

    class Meta:
        model = Member
        fields = ("username", "first_name", "last_name", "email", "city", "country", "password1", "password2")

    def clean_username(self):
        username = self.cleaned_data["username"]
        try:
            Member.objects.get(username=username)
        except Member.DoesNotExist:
            return username
        raise forms.ValidationError(
            self.error_messages['duplicate_username'],
            code='duplicate_username',
        )


class ClubForm(forms.ModelForm):

    class Meta:
        model = Club
        fields = ("name", "member", "description")


class DishForm(forms.ModelForm):

    class Meta:
        model = Dish
        fields = ("name", "restaurant")


class RestaurantForm(forms.ModelForm):

    class Meta:
        model = Restaurant
        fields = ("name", "group", "city", "country", "description")

