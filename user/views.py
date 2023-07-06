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


# class Register(APIView):
#     authentication_classes = []
#     permission_classes = []

#     def post(self, request):
#         serializer = UserSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = []
    permission_classes = []

    # Creates User
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=201, headers=headers)
    
    

class HackathonRegistrationAPIView(APIView):
    permission_classes = [IsAuthenticated]

    # registers the user to a hackathon
    def post(self, request):
        hackathon_id = request.data['hackathon_id']
        if not hackathon_id:
            raise ValidationError("Hackathon id is required")

        try:
            hackathon = Hackathon.objects.get(id=hackathon_id)
        except Hackathon.DoesNotExist:
            raise ValidationError("Invalid Hackathon ID")

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
        hackathon_data = [{
            'title': hackathon.title,
            'description': hackathon.description,
            'submission_type': hackathon.submission_type,
            'start_datetime': hackathon.start_datetime,
            'end_datetime': hackathon.end_datetime,
        } for hackathon in hackathons]
        return JsonResponse({'registered_hackathons': hackathon_data})
  
