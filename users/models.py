from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    """Extends the User model to include roles"""
    ROLE_CHOICES = [
        ('general_manager', 'General Manager'),
        ('production_manager', 'Production Manager'),
        ('sales_manager', 'Sales Manager'),
        ('employee', 'Employee')
    ]
    
    role = models.CharField(max_length=50, choices=ROLE_CHOICES, default='employee')

    # Resolved the conflict by adding related_name
    groups = models.ManyToManyField(
        "auth.Group",
        related_name="custom_users_groups",  # Adding a unique related_name
        blank=True
    )
    
    user_permissions = models.ManyToManyField(
        "auth.Permission",
        related_name="custom_users_permissions",  # Adding a unique related_name
        blank=True
    )

    def __str__(self):
        return f"{self.username} - {self.role}"
