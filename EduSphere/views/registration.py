from rest_framework import status, views, response
from rest_framework.permissions import IsAuthenticated
from authentication.custom_permissions import IsAuthorized
from authentication.custom_authentication import CustomAuthentication

from Utility.upload_to_gcs import image_upload_to_gcs

from EduSphere.models.School import School
from EduSphere.serializers.school_serializer import SchoolCreateSerializer

class SchoolRegistrationAPIView(views.APIView):

    def get(self, request,format=None,pk=None, *args, **kwargs):
        try:
            Schools=School.objects.all()
            serializer=SchoolCreateSerializer(Schools,many=True)
            return response.Response(serializer.data)
        
        except ValueError as e:
            return response.Response({'message': str(e)},
                                     status=status.HTTP_400_BAD_REQUEST)
            
        except Exception as e:
            return response.Response({'message': str(e)},
                                     status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, format=None):
        serializer = SchoolCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response({'message': 'Data Created'}, status=status.HTTP_201_CREATED)
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):
        try:
            school = School.objects.get(pk=pk)
        except School.DoesNotExist:
            return response.Response({'message': 'School not found'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = SchoolCreateSerializer(school, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response({'message': 'Complete Data Updated'})
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk, format=None):
        try:
            school = School.objects.get(pk=pk)
        except School.DoesNotExist:
            return response.Response({'message': 'School not found'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = SchoolCreateSerializer(school, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return response.Response({'message': 'Partial Data Updated'})
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        try:
            school = School.objects.get(pk=pk)
        except School.DoesNotExist:
            return response.Response({'message': 'School not found'}, status=status.HTTP_404_NOT_FOUND)
        
        school.delete()
        return response.Response({'message': 'Data Deleted'})



from EduSphere.forms.form import addressform,Schoolform 
from django.shortcuts import redirect,render 

def addon(request):
    address_form=addressform(request.POST or None)
    school_form=Schoolform(request.POST or None)
    if addressform.is_valid and school_form.is_valid():
        address_form.save()
        school_form.save()
    context = {
        'address_form': address_form,
        'school_form': school_form,
    }
    
    return render(request, 'templates.html', context)
