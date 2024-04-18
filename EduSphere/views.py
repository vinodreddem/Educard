from django.shortcuts import render

from rest_framework import viewsets
from EduSphere.models import *

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serlizers import Classsesrlizere
from .serlizers import CLS_SUBJ_MSTR_serlizere
from .serlizers import MstClassserlizere
from .serlizers import MstSubjectserlizere
from .serlizers import schoolserlizere
from .serlizers import Subjectserlizere
from .serlizers import Teacherserlizere


from .models.Class import Classes
from .models.Master import MstClass
from .models.Master import MstSubject#MstPaymentStatus
from .models.School import Schools
from .models.Subject import Subjects
from .models.Teacher import Teachers
from .models.cls_subj_mstr import CLS_SUBJ_MSTR
# Create your views here."""
#from rest_framework.authentication import SessionAuthentication
#from rest_framework.permissions import IsAuthenticated
"""def home(request):
    student_obj=Classes.objects.all()

    serializer=Studentserlizere(student_obj,many=True)

    return Response({'status':200,'payload':serializer.data})
"""
"""
class ClassesViewset(viewsets.ModelViewSet):
    queryset=Classes.objects.all()
    serializer_class=Classsesrlizere
    #authentication_classes=[SessionAuthentication]
    #permission_classes=[IsAuthenticated]

class CLS_SUBJ_MSTRViewset(viewsets.ModelViewSet):
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

class Clas(APIView): 
    def get(self, request):
        clsobj=Classes.objects.all()
        serializer=Classsesrlizere(clsobj,many=True)
        return Response(serializer.data)

    def post(self, request):
        clsobj=Classes.objects.all()
        serializer=Classsesrlizere(data=clsobj.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

    def put(request,id):
        clsobj=Classes.objects.get(id=id)
        serializer=Classsesrlizere(instance=clsobj,data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

    def delete(request,id):
        clsobj=Classes.objects.get(id=id)
        clsobj.delete()
        return Response('student is deleted')



class Cls_Subj_mstr(APIView):
    def get(self,request): 
        clsobj=CLS_SUBJ_MSTR.objects.all()
        serializer=CLS_SUBJ_MSTR_serlizere(clsobj,many=True)
        return Response(serializer.data)

    def post(self,request):
        clsobj=CLS_SUBJ_MSTR.objects.all()
        serializer=CLS_SUBJ_MSTR_serlizere(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

    def put(self,request,id):
        clsobj=CLS_SUBJ_MSTR.objects.get(id=id)
        serializer=CLS_SUBJ_MSTR_serlizere(instance=clsobj,data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

    def delete(self,request,id):
        clsobj=CLS_SUBJ_MSTR.objects.get(id=id)
        clsobj.delete()
        return Response('student is deleted')



class MstClassser(APIView):
    def get(self,request): 
        clsobj=MstClass.objects.all()
        serializer=MstClassserlizere(clsobj,many=True)
        return Response(serializer.data)

    def post(self,request):
        clsobj=MstClass.objects.all()
        serializer=MstClassserlizere(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

    def put(self,request,id):
        clsobj=MstClass.objects.get(id=id)
        serializer=MstClassserlizere(instance=clsobj,data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

    def delete(self,request,id):
        clsobj=MstClass.objects.get(id=id)
        clsobj.delete()
        return Response('student is deleted')



class MstSubject(APIView):
    def get(self,request): 
        clsobj=MstSubject.objects.all()
        serializer=MstSubjectserlizere(clsobj,many=True)
        return Response(serializer.data)

    def post(self,request):
        clsobj=MstSubject.objects.all()
        serializer=MstSubjectserlizere(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

    def put(self,request,id):
        clsobj=MstSubject.objects.get(id=id)
        serializer=MstSubjectserlizere(instance=clsobj,data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

    def delete(self,request,id):
        clsobj=MstSubject.objects.get(id=id)
        clsobj.delete()
        return Response('student is deleted')



class school(APIView):
    def get(self,request): 
        clsobj=Schools.objects.all()
        serializer=schoolserlizere(clsobj,many=True)
        return Response(serializer.data)

    def post(self,request):
        clsobj=Schools.objects.all()
        serializer=schoolserlizere(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

    def put(self,request,id):
        clsobj=CLS_SUBJ_MSTR.objects.get(id=id)
        serializer=Schools(instance=clsobj,data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

    def delete(self,request,id):
        clsobj=Schools.objects.get(id=id)
        clsobj.delete()
        return Response('student is deleted')



class Subject(APIView):
    def get(self,request): 
        clsobj=Subjects.objects.all()
        serializer=Subjectserlizere(clsobj,many=True)
        return Response(serializer.data)

    def post(self,request):
        clsobj=Subjects.objects.all()
        serializer=Subjectserlizere(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

    def put(self,request,id):
        clsobj=Subjects.objects.get(id=id)
        serializer=Subjectserlizere(instance=clsobj,data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

    def delete(self,request,id):
        clsobj=Subjects.objects.get(id=id)
        clsobj.delete()
        return Response('student is deleted')


class Teacher(APIView):
    def get(self,request): 
        clsobj=Teachers.objects.all()
        serializer=Teacherserlizere(clsobj,many=True)
        return Response(serializer.data)

    def post(self,request):
        clsobj=Teachers.objects.all()
        serializer=Teacherserlizere(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

    def put(self,request,id):
        clsobj=Teachers.objects.get(id=id)
        serializer=Teacherserlizere(instance=clsobj,data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

    def delete(self,request,id):
        clsobj=Teachers.objects.get(id=id)
        clsobj.delete()
        return Response('student is deleted')