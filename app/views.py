from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics
from django.shortcuts import get_object_or_404
global data;
data = ['tst']
class myapi(APIView):
    def get(self, request,format=None):
        msg={
            'Response': 200,
            'Msg':"welcome "
        }
        return Response(msg)

    def post(self, request, format=None):
        datam = request.data
        name =datam.get('name',None)
        data.append(name)
        msg = {
            'Response': 200,
            'Msg': "welcome ",
            'data' :data
        }
        return Response(msg)


# Create your views here.
