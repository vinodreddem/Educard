
from django.contrib import admin
from django.urls import path,include
from rest_framework import routers

from EduSphere import views

from EduSphere.views import ClassesViewset
from EduSphere.views import CLS_SUBJ_MSTRViewset
from EduSphere.views import MstClassViewset
from EduSphere.views import MstSubjectViewset
from EduSphere.views import TeachersViewset
from EduSphere.views import SubjectsViewset
from EduSphere.views import schoolsViewset



router=routers.DefaultRouter()
router.register('api',views.ClassesViewset,basename=ClassesViewset)
router.register('CLS_SUBJ_MSTR/',CLS_SUBJ_MSTRViewset)
router.register('MstClass/',MstClassViewset)
router.register('MstSubject/',MstSubjectViewset)
router.register('schools/',schoolsViewset)
router.register('Subjects/',SubjectsViewset)
router.register('Teachers/',TeachersViewset)


urlpatterns = [
    path('admin/', admin.site.urls),

    path('',include(router.urls)),#path('nani/', nani, name='nani'),

]