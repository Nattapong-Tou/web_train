from django.contrib import admin
from django.urls import path, re_path
from .views import * 


urlpatterns = [
    # static path
    path('', home, name='home_page'),
    path('about/', about, name='about_page'),
    path('map/', map, name='map_page'),
    path('variable/', variable, name='variable_page'),
    path('tag_if/', tag_if, name='tag_if_page'),
    path('tag_loop/', tag_loop, name='tag_loop_page',),
    path('filter_sample/', filter_sample, name='filter_sample_page'),
    path('filter_number/', filter_number, name='filter_number_page'),
    path('filter_url/', filter_url,name='filter_url_page'),

    # parameter path
    path('search/<str:keyword>/<int:page>', search, name='search_parameter_page'),
    path('date/<int:day>/<int:month>/<int:year>', date, name='date_parameter_page'),
    
    # regular expression path
    re_path('^drink/(?P<drink>(coffee)|(tea)|(milk)|(wine))/$', drink, name='drink_regular_page'),
    re_path(r'^find/(?P<key>[\W\S]+)/(?P<page>\d+)/$', find_page, name='find_regular_page'),
    
]