from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class AnimalType(models.Model):
    """Defines the type of animals (e.g., Pigs, Chickens)"""
    name = models.CharField(max_length=50, unique=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return self.name
    
class AnimalBreed(models.Model):
    """Defines different breeds for each animal type (e.g., Large White, Landrace)"""
    animal_type = models.ForeignKey(AnimalType, on_delete=models.CASCADE, related_name="breeds")
    name = models.CharField(max_length=50)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return f"{self.name} ({self.animal_type.name})"
    
class WeightCategory(models.Model):
    """Defines weight categories for animals (e.g., 5-10kg, 11-20kg)"""
    min_weight = models.FloatField()
    max_weight = models.FloatField()
    
    def __str__(self):
        return f"{self.min_weight}-{self.max_weight} kg"

class AnimalGroup(models.Model):
    """Represents a group of animals with shared characteristics"""
    animal_type = models.ForeignKey(AnimalType, on_delete=models.CASCADE, related_name="animal_groups")
    breed = models.ForeignKey(AnimalBreed, on_delete=models.CASCADE, related_name="animal_groups")
    gender = models.CharField(max_length=10, choices=[('male', 'Male'), ('female', 'Female')])
    quantity = models.IntegerField()
    birth_date = models.DateField()
    weight = models.FloatField()
    weight_category = models.ForeignKey(WeightCategory, on_delete=models.SET_NULL, null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="animal_groups")
    
    def save(self, *args, **kwargs):
        """Automatically assigns a weight category"""
        categories = WeightCategory.objects.all()
        for category in categories:
            if category.min_weight <= self.weight <= category.max_weight:
                self.weight_category = category
                break
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.quantity} {self.breed.name} ({self.animal_type.name}) - {self.weight_category}"
    
class BirthRecord(models.Model):
    """Records birth events in the farm"""
    parent_animal = models.ForeignKey(AnimalGroup, on_delete=models.CASCADE, related_name="births")
    birth_date = models.DateField()
    number_of_offspring = models.IntegerField()
    male_count = models.IntegerField()
    female_count = models.IntegerField()
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"Birth {self.parent_animal.breed.name} ({self.birth_date})"

class HealthRecord(models.Model):
    """Tracks the health status of animals"""
    animal = models.ForeignKey(AnimalGroup, on_delete=models.CASCADE, related_name="health_records")
    checkup_date = models.DateField(auto_now_add=True)
    diagnosis = models.TextField()
    treatment = models.TextField()
    veterinarian = models.CharField(max_length=100)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"Health Check {self.animal.breed.name} - {self.checkup_date}"

class FeedingRecord(models.Model):
    """Tracks farm resources such as food, water, and medication"""
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=50, choices=[('food', 'Food'), ('water', 'Water'), ('medicine', 'Medicine')])
    stock_quantity = models.FloatField()

    def __str__(self):
        return f"{self.name} - {self.type} ({self.stock_quantity})"