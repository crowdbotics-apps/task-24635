from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import (
    TaskerAvailabilityViewSet,
    TaskerSkillViewSet,
    TimeslotViewSet,
    BusinessPhotoViewSet,
)

router = DefaultRouter()
router.register("taskerskill", TaskerSkillViewSet)
router.register("timeslot", TimeslotViewSet)
router.register("taskeravailability", TaskerAvailabilityViewSet)
router.register("businessphoto", BusinessPhotoViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
