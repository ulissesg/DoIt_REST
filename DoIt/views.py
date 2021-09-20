from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *

from DoIt.models import List


class Lists(APIView):

    def get(self, request):
        lis = List.objects.all()
        serializer = ListSerializer(lis, many=True)
        return Response(serializer.data)

    def post(self):
        pass


class Tasks(APIView):

    def get(self, request):
        task = Task.objects.all()
        serializer = TaskSerializer(task, many=True)
        return Response(serializer.data)

    def post(self):
        pass
