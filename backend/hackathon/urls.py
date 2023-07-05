

from django.urls import path, include
from rest_framework import routers

from .views import SubmissionViewset

router = routers.DefaultRouter()
router.register(r"submission", SubmissionViewset)

urlpatterns = [
    path('', include(router.urls)),
]
