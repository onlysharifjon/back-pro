from django.shortcuts import render



from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ApplicationSerializer

class SaveDataAPI(APIView):
    def post(self,request):
        serializer = ApplicationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Malumot qoshildi'})
        else:
            return Response(serializer.errors)

