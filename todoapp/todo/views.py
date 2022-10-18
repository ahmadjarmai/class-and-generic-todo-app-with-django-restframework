from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics

from todo.api.serializer import TodoSerializer
from .models import Todo

class TodoApiView(APIView) :
    def get(self, request, *args, **kwargs) :
        persons =Todo.objects.all()
        serializer =TodoSerializer(persons, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer =TodoSerializer(data=request.data)
        if serializer.is_valid() :
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

class TodoDetail(APIView) :

    def get(self, request, pk, format=None) :
        person =get_object_or_404(Todo, id =pk)
        serializer =TodoSerializer(person)
        return Response(serializer.data)
    
    def put(self,request, pk, format=None) :
        person =get_object_or_404(Todo, id=pk)
        serializer =TodoSerializer(instance =person, data=request.data)
        if serializer.is_valid() :
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_404_BAD_REQUEST)

    def delete(self, request, pk, format=None) :
        person =get_object_or_404(Todo, id=pk)
        person.delete()
        return Response(status =status.HTTP_204_NO_CONTENT)



class TodoListCreate(generics.ListCreateAPIView) :
    queryset =Todo.objects.all()
    serializer_class =TodoSerializer

class TodoUdateRetriveDelete(generics.RetrieveUpdateDestroyAPIView) :
    queryset =Todo.objects.all()
    serializer_class =TodoSerializer

