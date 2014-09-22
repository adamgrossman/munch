from django.contrib.auth.models import AbstractUser
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models


class Member(AbstractUser):
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

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
    country = models.CharField(max_length=100)
    group = models.ManyToManyField(Club, related_name="restaurants")

    def __unicode__(self):
        return self.name


class Dish(models.Model):
    name = models.CharField(max_length=150)
    restaurant = models.ForeignKey(Restaurant, related_name="dish")

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

#
# class Picture(models.Model):
#     image = models.ImageField(upload_to='img', blank=True, null=True)


#
# class Tag(models.Model):
#     name = models.CharField(max_length=30)
#     restaurants = models.ManyToManyField(Restaurant, related_name="restauranttags")
#     dishes = models.ManyToManyField(Dish, related_name="dishtags")
#
#     def __unicode__(self):
#         return self.name