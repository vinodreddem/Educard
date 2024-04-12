from django.contrib import admin

# Register your models here.

from .modelsf.Class import Classes
from .modelsf.cls_subj_mstr import CLS_SUBJ_MSTR
from .modelsf.Master import MstSubject
from .modelsf.Master import MstClass#MstPaymentStatus
from .modelsf.Master import MstPaymentStatus
from .modelsf.School import Schools
from .modelsf.Subject import Subjects
from .modelsf.Teacher import Teachers


admin.site.register(Classes)
admin.site.register(CLS_SUBJ_MSTR)
admin.site.register(MstSubject)
admin.site.register(MstClass)
#admin.site.register(Schools)
admin.site.register(Subjects)
admin.site.register(Teachers)


