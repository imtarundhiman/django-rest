from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from . import serializers
from rest_framework import status

# Create your views here.

class HelloApiView(APIView):
    """ Test Api View. """

    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """ Returns a list of ApiView features """

        an_apiview = [
            'uses HTTP methods as function (get,post,patch,put,delete)',
            'it is similiar to a traditional Django view',
            'Is mapped manually to URLs'
        ]

        response = {
            'message':'Hello !',
            'an_apiview': an_apiview
        }

        return Response(response)

    def post(self, request):
        """ Create a hello mesage with our name. """   

        serializer = serializers.HelloSerializer(data=request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            message  = 'Hello {0}'.format(name)
            return Response({'message' : message})

        else: 
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        """ Handles updating an object. """

        return Response({'method': 'put'})

    def patch(self, request, pk=None):
        """ Patch request, only updates fields provided in the request """

        return Response({'method': 'patch'})


    def delete(self, request, pk=None):
        """ Deletes the object. """

        return Response({'method': 'delete'})
