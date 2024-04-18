from rest_framework import serializers
from EduSphere.models import *

from .models.Class import Classes
from .models.cls_subj_mstr import CLS_SUBJ_MSTR
from .models.Master import MstClass
from .models.Master import MstSubject
from .models.School import Schools
from .models.Subject import Subjects
from .models.Teacher import Teachers


class Classsesrlizere(serializers.ModelSerializer):
    class Meta:
        model=Classes
        fields = ['uuid','class_id','school_id','Description']

class CLS_SUBJ_MSTR_serlizere(serializers.ModelSerializer):
    class Meta:
        model=CLS_SUBJ_MSTR
        fields = '__all__'

class MstClassserlizere(serializers.ModelSerializer):
    class Meta:
        model=MstClass
        fields = '__all__'

class MstSubjectserlizere(serializers.ModelSerializer):
    class Meta:
        model=MstSubject
        fields = '__all__'

class schoolserlizere(serializers.ModelSerializer):
    class Meta:
        model=Schools
        fields = '__all__'

class Subjectserlizere(serializers.ModelSerializer):
    class Meta:
        model=Subjects
        fields = '__all__'

class Teacherserlizere(serializers.ModelSerializer):
    class Meta:
        model=Teachers
        fields = '__all__'
