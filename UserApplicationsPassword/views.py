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
        info = UserApplicationpss.objects.all().filter(user_key=user_name)
        serializer = ApplicationSerializer(info, many=True).data
        return Response(serializer)


class FilterBYApp(APIView):
    queryset = UserApplicationpss.objects.all()

    def post(self, request):
        app_name = request.data.get("application")
        get_all_pass = UserApplicationpss.objects.all().filter(application=app_name)
        serializer = ApplicationSerializer(get_all_pass, many=True).data
        return Response(serializer)


class AddUser(APIView):
    queryset = UserApplicationpss.objects.all()
    serializer = Sort_srl()


    def post(self, request):

        re_password = request.data.get("password")
        pass_count = UserApplicationpss.objects.all().filter(password=re_password).count()
        if pass_count >= 2:
            serializer = Sort_srl(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"MSG": "Succsesfuly"})
            else:
                return Response(serializer.errors)
        else:
            return Response({"ERROR": "BOSHQA PASS KIRIT"})
        
        