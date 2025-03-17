from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import (
    AnimalType, AnimalBreed, AnimalGroup, WeightCategory,
    BirthRecord, HealthRecord, FeedingRecord
)
from .serializers import (
    AnimalTypeSerializer, AnimalBreedSerializer, AnimalGroupSerializer, WeightCategorySerializer,
    BirthRecordSerializer, HealthRecordSerializer, FeedingRecordSerializer
)

class AnimalTypeViewSet(viewsets.ModelViewSet):
    queryset = AnimalType.objects.all()
    serializer_class = AnimalTypeSerializer
    permission_classes = [IsAuthenticated]    
    
    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user) 

class AnimalBreedViewSet(viewsets.ModelViewSet):
    queryset = AnimalBreed.objects.all()
    serializer_class = AnimalBreedSerializer
    permission_classes = [IsAuthenticated]

class AnimalGroupViewSet(viewsets.ModelViewSet):
    queryset = AnimalGroup.objects.all()
    serializer_class = AnimalGroupSerializer
    permission_classes = [IsAuthenticated]

class WeightCategoryViewSet(viewsets.ModelViewSet):
    queryset = WeightCategory.objects.all()
    serializer_class = WeightCategorySerializer
    permission_classes = [IsAuthenticated]

class BirthRecordViewSet(viewsets.ModelViewSet):
    queryset = BirthRecord.objects.all()
    serializer_class = BirthRecordSerializer
    permission_classes = [IsAuthenticated]

class HealthRecordViewSet(viewsets.ModelViewSet):
    queryset = HealthRecord.objects.all()
    serializer_class = HealthRecordSerializer
    permission_classes = [IsAuthenticated]

class FeedingRecordViewSet(viewsets.ModelViewSet):
    queryset = FeedingRecord.objects.all()
    serializer_class = FeedingRecordSerializer
    permission_classes = [IsAuthenticated]
