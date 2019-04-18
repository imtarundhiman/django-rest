from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

class HelloApiView(APIView):
    """ Test Api View. """

    def get(self, request, format=None):
        """ Returns a list of ApiView features """

        an_apiview = [
            'uses HTTP methods as function (get,post,patch,put,delete)',
            'it is similiar to a traditional Django view',
            'Is mapped manually to URLs'
        ]

        return Response({
            'message':'Hello !',
            'an_apiview': an_apiview
        })