from django.shortcuts import render

from rest_framework import viewsets
from EduSphere.modelsf import *

#from rest_framework.decorators import api_view
#from rest_framework.response import Response

from .serlizers import Classsesrlizere
from .serlizers import CLS_SUBJ_MSTR_serlizere
from .serlizers import MstClassserlizere
from .serlizers import MstSubjectserlizere
from .serlizers import schoolserlizere
from .serlizers import Subjectserlizere
from .serlizers import Teacherserlizere



from .modelsf.Class import Classes
"""from models1.Master import MstSubject,MstClass#MstPaymentStatus
from models1.School import Schools
from models1.Subject import Subjects
from models1.Teacher import Teachers
from models1.cls_subj_mstr import CLS_SUBJ_MSTR
# Create your views here."""

"""def home(request):
    student_obj=Classes.objects.all()

    serializer=Studentserlizere(student_obj,many=True)

    return Response({'status':200,'payload':serializer.data})
"""

class ClassesViewset(viewsets.ModelViewSet):
    queryset=Classes.objects.all()
    serializer_class=Classsesrlizere

"""class CLS_SUBJ_MSTRViewset(viewsets.ModelViewSet):
    queryset=CLS_SUBJ_MSTR.objects.all()
    serializer_class=CLS_SUBJ_MSTR_serlizere

class MstClassViewset(viewsets.ModelViewSet):
    queryset=MstClass.objects.all()
    serializer_class=MstClassserlizere

class MstSubjectViewset(viewsets.ModelViewSet):
    queryset=MstSubject.objects.all()
    serializer_class=MstSubjectserlizere

class schoolsViewset(viewsets.ModelViewSet):
    queryset=Schools.objects.all()
    serializer_class=schoolserlizere

class SubjectsViewset(viewsets.ModelViewSet):
    queryset=Subjects.objects.all()
    serializer_class=Subjectserlizere

class TeachersViewset(viewsets.ModelViewSet):
    queryset=Teachers.objects.all()
    serializer_class=Teacherserlizere"""