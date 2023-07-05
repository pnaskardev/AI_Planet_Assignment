

from django.urls import path, include
from rest_framework import routers
from . import views
from .views import SubmissionViewset

router = routers.DefaultRouter()
router.register(r"submission", SubmissionViewset)

urlpatterns = [
    path('hackathons/', views.HackathonListAPIView.as_view(),name='hackathon-list'),
    path('', include(router.urls)),
]
