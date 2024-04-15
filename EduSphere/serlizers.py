from rest_framework import serializers
from EduSphere.modelsf import *

from .modelsf.Class import Classes
from .modelsf.cls_subj_mstr import CLS_SUBJ_MSTR
from .modelsf.Master import MstClass
from .modelsf.Master import MstSubject
from .modelsf.School import Schools
from .modelsf.Subject import Subjects
from .modelsf.Teacher import Teachers


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
