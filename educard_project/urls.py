
from django.contrib import admin
from django.urls import path,include
#from rest_framework import routers
from EduSphere import views

from EduSphere.views import *

"""from EduSphere.views import CLS_SUBJ_MSTRViewset
from EduSphere.views import MstClassViewset
from EduSphere.views import MstSubjectViewset
from EduSphere.views import TeachersViewset
from EduSphere.views import SubjectsViewset
from EduSphere.views import schoolsViewset

"""

"""router=routers.DefaultRouter()
router.register('api',views.ClassesViewset,basename=ClassesViewset)
router.register('CLS_SUBJ_MSTR/',CLS_SUBJ_MSTRViewset)
router.register('MstClass/',MstClassViewset)
router.register('MstSubject/',MstSubjectViewset)
router.register('schools/',schoolsViewset)
router.register('Subjects/',SubjectsViewset)
router.register('Teachers/',TeachersViewset)
"""

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('api/', views.Clas.as_view()),
    path('api/<int:id>/', views.Clas.as_view()),
    
    path('api1/', views.Cls_Subj_mstr.as_view()),
    path('api1/<int:id>/', views.Cls_Subj_mstr.as_view()),
    
    path('api2/', views.MstClassser.as_view()),
    path('api/<int:id>/', views.MstClassser.as_view()),
    
    path('api3/', views.MstSubject.as_view()),
    path('api3/<int:id>/', views.MstSubject.as_view()),
    
    path('api4/', views.school.as_view()),
    path('api4/<int:id>/', views.school.as_view()),
    
    path('api5/', views.Subject.as_view()),
    path('api5/<int:id>/', views.Subject.as_view()),
    
    path('api6/', views.Teacher.as_view()),
    path('api6/<int:id>/', views.Teacher.as_view()),

#    path('',include(router.urls)),#path('nani/', nani, name='nani'),
 #   path('auth/',include('rest_framework.urls')),#path('nani/', nani, name='nani'),

]