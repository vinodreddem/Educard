<<<<<<< HEAD
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
=======
from .Master import MstSubject
from .Class import Class

class Subject(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    subject_id = models.ForeignKey(MstSubject, on_delete=models.DO_NOTHING)
    class_id = models.ForeignKey(Class, on_delete=models.CASCADE)
    Description = models.CharField(max_length=100)

    def __str__(self):
        pass    
>>>>>>> master
