from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework import routers
from . import views


router = routers.DefaultRouter()
router.register(r"register", views.UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register_hackathon/', views.HackathonRegistrationAPIView.as_view(), name='registered_hackathons'),
    path('registered_hackathons/', views.ListRegisteredHackathons.as_view(), name='registered_hackathons'),
]
