from django.db import models

# Create your models here.
from django.db import models


class Contact(models.Model):
    full_name = models.CharField(max_length=255)
    email = models.EmailField()
    contact = models.CharField(max_length=20)
    message = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.full_name