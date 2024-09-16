from django.contrib import admin

# Register your models here.

from .models.Class import Classes
from .models.cls_subj_mstr import CLS_SUBJ_MSTR
from .models.Master import MstSubject
from .models.Master import MstClass#MstPaymentStatus
from .models.Master import MstPaymentStatus
from .models.School import Schools
from .models.Subject import Subjects
from .models.Teacher import Teachers


admin.site.register(Classes)
admin.site.register(CLS_SUBJ_MSTR)
admin.site.register(MstSubject)
admin.site.register(MstClass)
admin.site.register(Schools)
admin.site.register(Subjects)
admin.site.register(Teachers)


