from django.db import models
from django.utils import timezone

class CLS_SUBJ_MSTR(models.Model):
    SCHOOL_ID = models.IntegerField()
    CLASS_ID = models.IntegerField()
    TeacherID = models.IntegerField()
    SubjectID = models.IntegerField()
    CR_DT = models.DateTimeField(default=timezone.now)  # Automatically set the creation date/time
    UP_DT = models.DateTimeField(default=timezone.now)      # Automatically update the date/time when the object is saved
