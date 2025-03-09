from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    AnimalTypeViewSet, AnimalBreedViewSet, AnimalGroupViewSet, WeightCategoryViewSet,
    BirthRecordViewSet, HealthRecordViewSet, FeedingRecordViewSet
)

router = DefaultRouter()
router.register(r'animal-types', AnimalTypeViewSet)
router.register(r'animal-breeds', AnimalBreedViewSet)
router.register(r'animal-groups', AnimalGroupViewSet)
router.register(r'weight-categories', WeightCategoryViewSet)
router.register(r'birth-records', BirthRecordViewSet)
router.register(r'health-records', HealthRecordViewSet)
router.register(r'feeding-records', FeedingRecordViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
