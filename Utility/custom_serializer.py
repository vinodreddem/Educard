from django.contrib.auth.models import Permission
from rest_framework.serializers import ModelSerializer
from rest_framework.fields import empty
from rest_framework.exceptions import PermissionDenied

class BaseSerializer(ModelSerializer):

    request_method_permission_codename_mapping = {
        "post":"add_{}",
        "patch":"change_{}",
        "put":"change_{}",
        "delete":"delete_{}",
        "get":"view_{}",
    }

    def __init__(self, instance=None, data=empty, request=None, **kwargs):
        super().__init__(instance, data, **kwargs)
        if request is None and 'context' in kwargs:
            request = kwargs.get('context').get('request',None)
        self.request = request
        if not self.is_authorized():
            raise PermissionDenied()

    def is_authorized(self):
        """
        Checking if user has permissions to access this model
        Permission should be assigned to the user or to the assigned groups
        """
        request_method = self.request.method.lower() if self.request else None
        user = self.request.user if self.request else None
        user_groups = user.groups.all() if user else []
        
        model_name = self.Meta.model.__name__.lower().replace(" ","")
        
        if request_method not in self.request_method_permission_codename_mapping.keys():
            return True

        permission_codename = self.request_method_permission_codename_mapping[request_method].format(model_name)

        # Checking if user groups has permissions assigned or not
        for each in user_groups:
            if each.permissions.filter(codename = permission_codename).exists():
                return True
        
        # Checking if user has direct permissions assigned
        if Permission.objects.filter(user__username=user.username, codename = permission_codename).exists():
            return True
        
        return False