from django.db import models


class MstActiveDirectoryUser():
    user_id = models.TextField(db_column='User_ID', primary_key=True, max_length=50)
    first_name = models.TextField(db_column='First_Name', blank=True, null=True)
    last_name = models.TextField(db_column='Last_Name', blank=True, null=True)
    full_name = models.TextField(db_column='Full_Name', blank=True, null=True)
    display_name = models.TextField(db_column='Display_Name', blank=True, null=True)
    email_id = models.EmailField(db_column='Email_ID', blank=True, null=True)
    designation = models.TextField(db_column='Designation', blank=True, null=True)
    telephone_number = models.TextField(db_column='Telephone_Number', blank=True, null=True)
    mobile_no = models.TextField(db_column='Mobile_NO', blank=True, null=True)
    address = models.TextField(db_column='Address', blank=True, null=True)
    city = models.TextField(db_column='City', blank=True, null=True)
    state = models.TextField(db_column='State', blank=True, null=True)
    postalcode = models.TextField(db_column='PostalCode', blank=True, null=True)
    country = models.TextField(db_column='Country', blank=True, null=True)

    def __str__(self):
          return f'{self.full_name}'

    class Meta:
        db_table = 'ACTIVE_DIRECTORY_USER'
        app_label = 'authentication'

def get_all_ad_users(request=None):
    query_set = MstActiveDirectoryUser.objects.all()
    return query_set

