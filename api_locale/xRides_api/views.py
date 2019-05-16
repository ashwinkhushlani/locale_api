from xRides_api.models import Rides
from xRides_api.serializers import xRidesSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class xRidesList(APIView):
    """
    List all rides, or create a new rides.
    """
    def get(self, request, format=None):
        xRides = Rides.objects.all()
        serializer = xRidesSerializer(xRides, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = xRidesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class xRidesDetail(APIView):
    """
    Retrieve, update or delete a rides instance.
    """
    def get_object(self, pk):
        try:
            return Rides.objects.get(pk=pk)
        except Rides.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        xRides = self.get_object(pk)
        serializer = xRidesSerializer(xRides)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        xRides = self.get_object(pk)
        serializer = xRidesSerializer(xRides, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        xRides = self.get_object(pk)
        xRides.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
