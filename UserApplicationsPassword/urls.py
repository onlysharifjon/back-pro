from django.urls import path,include
from .views import FilterbyUser

urlpatterns=[
    path("filter/",FilterbyUser.as_view())
]