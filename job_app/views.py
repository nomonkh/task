from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import TaskModel, ExecutorModel
from .serializers import ExecutorSerializer, TaskSerializer, SingleTaskSerializer


class TaskView(viewsets.ModelViewSet):
    queryset = TaskModel.objects.all()
    serializer_class = TaskSerializer

    def create(self, request):
        try:
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid():
                executor = request.data.pop('executor')
                ExecutorModel.objects.create(**executor)
                TaskModel.objects.create(**request.data, executor_id=executor.id)
                return Response({'msg': 'true'}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'msg': str(e)})


class SingleApiTask(viewsets.ModelViewSet):
    queryset = TaskModel.objects.all()
    serializer_class = SingleTaskSerializer

    def create(self, request):
        print(request.data)
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'true'}, status=status.HTTP_201_CREATED)
        return Response({'msg': 'false'})
