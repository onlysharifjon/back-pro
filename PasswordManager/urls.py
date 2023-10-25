from django.urls import path
from .views import index,PasswordLevel1

urlpatterns = [
    path('index/', index ),
    path('password/',PasswordLevel1.as_view()),
]