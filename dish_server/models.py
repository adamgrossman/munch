from django.contrib.auth.models import AbstractUser
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models


class Member(AbstractUser):
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='member_photos', blank=True, null=True, default='member_photos/me.jpg')

    def __unicode__(self):
        return self.username


class Club(models.Model):
    name = models.CharField(max_length=100)
    member = models.ManyToManyField(Member, related_name="clubs")
    description = models.TextField()

    def __unicode__(self):
        return self.name


class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=20, null=True)
    country = models.CharField(max_length=100)
    club = models.ManyToManyField(Club, related_name="restaurants")

    def __unicode__(self):
        return self.name


class Dish(models.Model):
    name = models.CharField(max_length=150)
    restaurant = models.ForeignKey(Restaurant, related_name="dish")
    price = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    course = models.CharField(max_length=50, null=True)
    photo = models.ImageField(upload_to='dish_photos', blank=True, null=True)

    def __unicode__(self):
        return self.name


class Comment(models.Model):
    body = models.TextField(max_length=400)
    author = models.ForeignKey(Member, related_name="comments")
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    def __unicode__(self):
        return u'{}'.format(self.body)
