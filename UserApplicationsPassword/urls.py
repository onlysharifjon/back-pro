from django.urls import path,include
from .views import FilterbyUser,SaveDataAPI,FilterbyInstaPassword

urlpatterns=[
    path("filter/",FilterbyUser.as_view()),
    path("save/", SaveDataAPI.as_view()),
    path("filter_password/", FilterbyInstaPassword.as_view()),
]