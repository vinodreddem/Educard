from rest_framework import status, views, response
from rest_framework.permissions import IsAuthenticated
from authentication.custom_permissions import IsAuthorized
from authentication.custom_authentication import CustomAuthentication


from Utility.upload_to_gcs import image_upload_to_gcs

class SchoolRegistrationAPIView(views.APIView):
    # authentication_classes = [CustomAuthentication]
    # permission_classes = [IsAuthenticated, IsAuthorized]
    request_user = None

    def initial(self, request, *args, **kwargs):
        self.request_user=request.user.username
        return super().initial(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        try:
            pass
        except ValueError as e:
            return response.Response({'message': str(e)},
                                     status=status.HTTP_400_BAD_REQUEST)
            
        except Exception as e:
            return response.Response({'message': str(e)},
                                     status=status.HTTP_400_BAD_REQUEST)

    def post():
        pass

    def put():
        pass

    def delete():
        pass


