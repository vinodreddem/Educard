from django.apps import apps

# Check if the app is registered
if apps.is_installed('EduSphere'):
    print("The app 'EduSphere' is registered.")
else:
    print("The app 'EduSphere' is not registered.")
