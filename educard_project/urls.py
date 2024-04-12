
from django.contrib import admin
from django.urls import path,include
from rest_framework import routers


from EduSphere.views import ClassesViewset
"""from EduSphere.views import CLS_SUBJ_MSTRViewset
from EduSphere.views import MstClassViewset
from EduSphere.views import MstSubjectViewse
from EduSphere.views import TeachersViewset
from EduSphere.views import SubjectsViewset
from EduSphere.views import schoolsViewse"""



router=routers.DefaultRouter()
router.register('classe',ClassesViewset)
"""router.register('CLS_SUBJ_MSTR/',CLS_SUBJ_MSTRViewset)
router.register('MstClass/',MstClassViewset)
router.register('MstClass/',MstSubjectViewse)
router.register('schools/',schoolsViewse)
router.register('Subjects/',SubjectsViewset)
router.register('Teachers/',TeachersViewset)"""


urlpatterns = [
    path('admin/', admin.site.urls),

    path('',include(router.urls)),]#path('nani/', nani, name='nani'),
"""    path('CLS_SUBJ_MSTR/',include(router.urls)),
    path('MstClass/',include(router.urls)),
    path('schools/',include(router.urls)),
    path('Subjects/',include(router.urls)),
    path('Teachers/',include(router.urls)),"""

