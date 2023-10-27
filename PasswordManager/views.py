import random
from .models import PasswordModel
from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import PasswordGeneratorSerializer
from rest_framework.response import Response


def index(request):
    return render(request, 'index.html')


# men

class PasswordLevel1(APIView):
    queryset = PasswordModel.objects.all()
    # Make sure to replace 'your_app_name' with your actual app name
    serializer = PasswordGeneratorSerializer

    def get(self, request):
        elements = ['a', 'b', 'c', 'd', 'e', 'f', 'g',
                    'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o']
        parolcha = ''

        for i in range(6):
            parolcha += random.choice(elements)
        for i in range(2):
            parolcha += random.randint(0, 9)
            

        return Response({'password': parolcha})


# alo

# Create your views here.
