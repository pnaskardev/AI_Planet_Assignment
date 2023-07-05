from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets

from .serializers import HackathonSerializer, SubmissionSerializer
from .models import Hackathon, Submission


class HackathonListAPIView(generics.ListAPIView):
    queryset = Hackathon.objects.all()
    serializer_class = HackathonSerializer


class HackathonRegistrationAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self,request,hackathon_id):
        hackathon = Hackathon.objects.get(id=hackathon_id)
        user = request.user
        hackathon.participants.add(user)
        hackathon.save()

        user.hackathons.add(hackathon)
        user.save()

        return Response({'message':'registered successfully'},status=200)
    

class SubmissionRegistration(viewsets.ModelViewSet):
    queryset=Submission.objects.all()
    serializer_class=SubmissionSerializer
    

