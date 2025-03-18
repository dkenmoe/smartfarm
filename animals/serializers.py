from rest_framework import serializers
from .models import (
    AnimalType, AnimalBreed, AnimalGroup, WeightCategory,
    BirthRecord, HealthRecord, FeedingRecord
)

class AnimalTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnimalType
        fields = ['id', 'name', 'created_by']
        read_only_fields = ['created_by']

class AnimalBreedSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnimalBreed
        fields = ['id', 'name', 'animal_type', 'created_by']
        read_only_fields = ['created_by']

class AnimalGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnimalGroup
        fields = '__all__'

class WeightCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = WeightCategory
        fields =  ['id', 'min_weight', 'max_weight', 'created_by']
        read_only_fields = ['created_by']

class BirthRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = BirthRecord
        fields = '__all__'
    
    def validate(self, data):
        """
        Ensure that the breed belongs to the selected animal type.
        """
        animal_type = data.get('animal_type')
        breed = data.get('breed')

        if breed and animal_type and breed.animal_type != animal_type:
            raise serializers.ValidationError("The selected breed does not belong to the specified animal type.")

        return data

class HealthRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = HealthRecord
        fields = '__all__'

class FeedingRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeedingRecord
        fields = '__all__'
