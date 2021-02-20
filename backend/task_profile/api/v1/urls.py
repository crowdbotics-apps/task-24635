from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import (
    TaskerProfileViewSet,
    InviteCodeViewSet,
    CustomerProfileViewSet,
    NotificationViewSet,
)

router = DefaultRouter()
router.register("taskerprofile", TaskerProfileViewSet)
router.register("customerprofile", CustomerProfileViewSet)
router.register("notification", NotificationViewSet)
router.register("invitecode", InviteCodeViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
