from django.urls import path,include
from .views import FilterbyUser, Filter2

urlpatterns=[
    path("filter/",FilterbyUser.as_view()),
    path("app/", Filter2.as_view())
]