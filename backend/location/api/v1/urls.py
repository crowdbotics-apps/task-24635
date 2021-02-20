from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import (
    TaskLocationViewSet,
    CustomerLocationViewSet,
    TaskerLocationViewSet,
    MapLocationViewSet,
)

router = DefaultRouter()
router.register("taskerlocation", TaskerLocationViewSet)
router.register("maplocation", MapLocationViewSet)
router.register("tasklocation", TaskLocationViewSet)
router.register("customerlocation", CustomerLocationViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
