from django.db import models
from .School import Schools
import uuid

class Teachers(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    school_id = models.ForeignKey(Schools, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    image_path = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name
