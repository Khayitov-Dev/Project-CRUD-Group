from django.urls import path
from crud.views import post_list


urlpatterns = [
    path('', post_list, name='post'),
]