from django.db import models
from .Master import MstClass
from .School import Schools
import uuid

class Class(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    class_id = models.ForeignKey(MstClass, on_delete=models.DO_NOTHING)
<<<<<<< HEAD
    school_id = models.ForeignKey(Schools, on_delete=models.DO_NOTHING)
=======
    school_id = models.ForeignKey(School, on_delete=models.CASCADE)
>>>>>>> master
    Description = models.CharField(max_length=100)

    #def __str__(self):
     #  pass