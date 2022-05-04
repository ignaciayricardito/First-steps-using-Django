from django.shortcuts import render

# Create your views here.

from rest_framework.response import Response
from rest_framework.views import APIView

class HelloWorld(APIView):
    def get(self, request):
        return Response(data="Hello, World !", status=200)
    

class PersonView(APIView):
    def get(self, request):
        return Response(data="Hola gente, estoy en el get", status=200)
    def post(self, request):
        return Response(data="Hola gente, estoy en el post", status=200)
    def patch(self, request):
        return Response(data="Hola gente, estoy en el path", status=200)
    def delete(self, request):
        return Response(data="Hola gente, estoy en el delete", status=200)
    