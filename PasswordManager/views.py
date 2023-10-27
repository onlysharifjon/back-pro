from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import PasswordGeneratorSerializer
from rest_framework.response import Response

def index(request):
    return render(request, 'index.html')


from .models import PasswordModel
import random

# men
class PasswordLevel1(APIView):
    queryset = PasswordModel.objects.all()
    serializer = PasswordGeneratorSerializer  # Make sure to replace 'your_app_name' with your actual app name

    def get(self, request):
        elements = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o']
        parolcha = ''
        for i in range(8):
            parolcha += random.choice(elements)

        return Response({'password': parolcha})


# alo

# Create your views here.
