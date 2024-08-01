from django import forms
from EduSphere.models.School import School
from EduSphere.models.Address import Address

class addressform(forms.ModelForm):
    class Meta:
        model=Address
        fields='__all__'

class Schoolform(forms.ModelForm):
    class Meta:
        model=School
        fields='__all__'