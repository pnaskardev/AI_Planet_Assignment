from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.permissions import IsAuthenticated

import jwt
import datetime

from .models import User


from .serializers import UserSerializer


class Register(APIView):
    authentication_classes = []
    permission_classes = []

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class RegisteredHackathons(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, reques):
        user = reques.user
        hackathons = user.hackathons.all()
        hackathon_data = [{
            'title': hackathon.title,
            'description': hackathon.description,
            'submission_type': hackathon.submission_type,
            'start_datetime': hackathon.start_datetime,
            'end_datetime': hackathon.end_datetime,
        } for hackathon in hackathons]
        return JsonResponse({'registered_hackathons': hackathon_data})
