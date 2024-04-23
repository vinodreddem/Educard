from django.db import models
from api.alias import AliasField
from api.models import BaseModel

def upload_file(instance, filename):
    """
    To generate for file upload path, This will need to change the path based on scenario, like School logo
    , Student Image or Teacher Image ..etc
    """
    # Check for filename generation If we upload pic directly from the Camera 
    return f"school/{instance.reference_object_id}/{filename}"


class Attachment(BaseModel):
    attachment_id = models.BigAutoField(db_column='ATTACHMENT_ID', primary_key=True)
    attachment_type = models.CharField(max_length=100, db_column='ATTACHMENT_TYPE') # like logo, classroom, park, play ground, etc..
    attachment_file = models.FileField(db_column='ATTACHMENT_FILE', upload_to=upload_file)
    reference_object_id = models.CharField(max_length=100, db_column='REFERENCE_OBJECT_ID') #school or teacher or student id
    reference_object_name = models.CharField(max_length=100, db_column='REFERENCE_OBJECT_NAME') # give some name for category of attachment 
    name = AliasField(db_column='ATTACHMENT_ID', blank=True, null=True)

    def __str__(self):
        return str(self.reference_object_id)

    class Meta:
        """
        Creating a table with specific name
        """
        db_table = 'ATTACHMENT'
