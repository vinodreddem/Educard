from django.db import models
import uuid

class Schools(models.Model):
    school_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)    
    phone = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(max_length=100, blank=True, null=True)
    image_path = models.CharField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=255)  
    country = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    district = models.CharField(max_length=50)
    town = models.CharField(max_length=50)
    pin = models.CharField(max_length=10)

    def __str__(self):
        return self.name
