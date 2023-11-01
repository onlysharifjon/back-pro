from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ApplicationSerializer, Sort_srl
from .models import UserApplicationpss
from PasswordManager.models import PasswordModel


class SaveDataAPI(APIView):
    def post(self, request):
        serializer = ApplicationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Malumot qoshildi'})
        else:
            return Response(serializer.errors)


class FilterbyUser(APIView):
    def post(self, request):
        user_name = request.data.get("password")
        print(user_name)
        id_s = PasswordModel.objects.all().filter(user=user_name)
        info = UserApplicationpss.objects.all().filter(user_key=2)
        serializer = ApplicationSerializer(info, many=True).data
        return Response(serializer)
