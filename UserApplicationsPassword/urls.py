from django.urls import path, include
from .views import *

urlpatterns = [
    path("Save/", SaveDataAPI.as_view),
    path("filter/", FilterbyUser.as_view()),
    path("appfilter/", FilterBYApp.as_view),
    path("add/", AddUser.as_view),
]
