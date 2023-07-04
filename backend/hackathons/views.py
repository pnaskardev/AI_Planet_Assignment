from django.shortcuts import render
from rest_framework import generics

from .models import Hackathon
from .serializers import HackathonSerializer

class HackathonListAPIView(generics.ListAPIView):
    queryset = Hackathon.objects.all()
    serializer_class = HackathonSerializer


