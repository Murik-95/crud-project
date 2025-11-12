from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Person
from .serializers import PersonSerializer
from django.shortcuts import get_object_or_404

class PersonListAPIView(APIView):
    def get(self, request):
        people = Person.objects.all()
        serializer = PersonSerializer(people, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PersonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors)

class PersonDetailAPIView(APIView):
    def get(self, request, pk):
        person = get_object_or_404(Person, pk=pk)
        serializer = PersonSerializer(person)
        return Response(serializer.data)

    def put(self, request, pk):
        person = get_object_or_404(Person, pk=pk)
        serializer = PersonSerializer(person, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, pk):
        person = get_object_or_404(Person, pk=pk)
        person.delete()
        return Response({'deleted': True})
