from django.db import models


class Address(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    address = models.CharField(max_length=255)  
    country = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    district = models.CharField(max_length=50)
    town = models.CharField(max_length=50)
    pin = models.CharField(max_length=10)