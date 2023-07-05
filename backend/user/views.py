from django.forms import ValidationError
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.permissions import IsAuthenticated

import jwt
import datetime

from hackathon.models import Hackathon

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


class HackathonRegistrationAPIView(APIView):
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
