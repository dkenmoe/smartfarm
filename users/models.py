from django.contrib.auth.models import AbstractUser
from django.db import models

class Role(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.name

class CustomUser(AbstractUser):
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True)
    
    def has_role(self, role_name):
        return self.role and self.role.name == role_name
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
