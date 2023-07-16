from django.forms import ValidationError
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated


from hackathon.models import Hackathon
from hackathon.serializers import HackathonSerializer

from .models import User


from .serializers import UserSerializer




class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = []
    permission_classes = []
    http_method_names=["post"]
    

class HackathonRegistrationAPIView(APIView):
    permission_classes = [IsAuthenticated]

    # registers the user to a hackathon
    def post(self, request):
        hackathon_id = request.data['hackathon_id']
        if not hackathon_id:
           return Response({'message': 'hackathon id not provided'}, status=400)

        try:
            hackathon = Hackathon.objects.get(id=hackathon_id)
        except Hackathon.DoesNotExist:
            return Response({'message': 'invalid hackathon id'}, status=400)

        user = request.user

        if hackathon in user.hackathons.all():
            return Response({'message': 'already registered'}, status=400)

        user.hackathons.add(hackathon)
        user.save()

        return Response({'message': 'registered successfully'}, status=200)

class ListRegisteredHackathons(APIView):
    permission_classes = [IsAuthenticated]

     # lists all the hackathons participated by the user 
    def get(self, request):
        user = request.user
        hackathons = user.hackathons.all()
        hackathon_data = HackathonSerializer(hackathons, many=True).data
        return JsonResponse({'registered_hackathons': hackathon_data})
  
