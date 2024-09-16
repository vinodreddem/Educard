from django.db import models
import uuid

<<<<<<< HEAD
class Schools(models.Model):
=======
from .Address import Address

class School(models.Model):
>>>>>>> master
    school_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)    
    phone = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(max_length=100, blank=True, null=True)
    # image_path = models.ImageField(upload_to='school_logos/', blank=True, null=True)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
