from django.db import models

class CLS_SUBJ_MSTR(models.Model):
    SCHOOL_ID = models.IntegerField()
    CLASS_ID = models.IntegerField()
    TeacherID = models.IntegerField()
    SubjectID = models.IntegerField()
    CR_DT = models.DateTimeField(auto_now_add=True)  # Automatically set the creation date/time
    UP_DT = models.DateTimeField(auto_now=True)      # Automatically update the date/time when the object is saved
