from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import UserRegisterSerializer,UserSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated


class Registerview(APIView):
    def post(self,request):
        seria=UserRegisterSerializer(data=request.data)
        if seria.is_valid():
            seria.save()
            return Response(seria.data,status=status.HTTP_200_OK)
        return Response(seria.errors,status=status.HTTP_400_BAD_REQUEST)
    
    
class Profileview(APIView):
    permission_classes=[IsAuthenticated]

    def get(self,request):
        seria=UserSerializer(request.user)
        return Response(seria.data,status=status.HTTP_200_OK)
    
    def patch(self,request):
        seria=UserSerializer(request.user,data=request.data,partial=True)
        if seria.is_valid():
            seria.save()
            return Response(seria.data,status=status.HTTP_200_OK)
        return Response(seria.errors,status=status.HTTP_400_BAD_REQUEST)
    
    
    

        

    
