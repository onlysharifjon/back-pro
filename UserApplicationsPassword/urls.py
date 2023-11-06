from django.urls import path, include
from .views import FilterbyUser, FilterBYApp

urlpatterns = [
    path("filter/", FilterbyUser.as_view()),
    path("application", FilterBYApp.as_view())

]
