from .Master import MstSubject
from .Class import Class

class Subject(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    subject_id = models.ForeignKey(MstSubject, on_delete=models.DO_NOTHING)
    class_id = models.ForeignKey(Class, on_delete=models.CASCADE)
    Description = models.CharField(max_length=100)

    def __str__(self):
        pass    