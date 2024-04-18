from django.db import models
from .School import Schools
import uuid

class Subjects(models.Model):
    subject_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    school_id = models.ForeignKey(Schools, on_delete=models.CASCADE)
    subject_name = models.CharField(max_length=50, blank=True, null=True)
    credits = models.IntegerField(null=True)
    image_path = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.subject_name
