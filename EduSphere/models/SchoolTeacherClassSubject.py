from django.db import models
import uuid

from .School import School
from .Class import Class
from .Subject import Subject
from .Teacher import Teacher

class SchoolTeacherClassSubject(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    school_id = models.ForeignKey(School, on_delete=models.CASCADE)
    class_id = models.ForeignKey(Class, on_delete=models.CASCADE)
    subject_id = models.ForeignKey(Subject, on_delete=models.CASCADE)
    teacher_id = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    

    class Meta:
        unique_together = ('school_id', 'class_id', 'subject_id', 'teacher_id')

    def __str__(self):
        return self.uuid
