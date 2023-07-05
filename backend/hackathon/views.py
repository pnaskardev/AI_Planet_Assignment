from rest_framework import status
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import viewsets
from rest_framework import permissions

from .serializers import HackathonSerializer, SubmissionSerializer
from .models import Hackathon, Submission


class HackathonListAPIView(generics.ListAPIView):
    queryset = Hackathon.objects.all()
    serializer_class = HackathonSerializer
    authentication_classes = []
    permission_classes = [AllowAny]


class SubmissionViewset(viewsets.ModelViewSet):
    queryset = Submission.objects.all()
    serializer_class = SubmissionSerializer

    def get(self, request):
        user = request.user
        submissions = Submission.objects.filter(user=user)
        serializer = SubmissionSerializer(submissions, many=True)
        return Response(serializer.data)

    def get_permissions(self):
        if self.request.method in permissions.SAFE_METHODS:
            return (permissions.AllowAny(),)

        if self.request.method == "POST":
            return (permissions.AllowAny(),)
