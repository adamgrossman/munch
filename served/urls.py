from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # HOME
    url(r'^$', 'dish_server.views.home', name='home'),
    url(r'^profile/$', 'dish_server.views.profile', name='profile'),

    # CLUBS
    url(r'^clubs/$', 'dish_server.views.clubs', name='clubs'),
    url(r'^clubs/new/$', 'dish_server.views.add_club', name='add_club'),
    # url(r'^clubs/(?P<club_id>\d+)/$', 'dish_server.views.view_club', name='view_club'),

    # RESTAURANTS
    url(r'^restaurants/$', 'dish_server.views.all_restaurants', name='restaurants'),
    url(r'^restuarants/new/$', 'dish_server.views.add_restaurant', name='add_restaurant'),

    # DISHES
    url(r'^munchies/$', 'dish_server.views.dishes', name='dishes'),
    url(r'^munchies/new/$', 'dish_server.views.add_dish', name='add_dish'),


    # REGISTRATION
    url(r'^register/$', 'dish_server.views.register', name='register'),
    url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', name='logout'),
    url(r'^password_reset/$', 'django.contrib.auth.views.password_reset', name='password_reset'),
    url(r'^password_reset/done/$', 'django.contrib.auth.views.password_reset_done', name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', 'django.contrib.auth.views.password_reset_confirm', name='password_reset_confirm'),
    url(r'^reset/done/$', 'django.contrib.auth.views.password_reset_complete', name='password_reset_complete'),

    url(r'^admin/', include(admin.site.urls)),

    )


