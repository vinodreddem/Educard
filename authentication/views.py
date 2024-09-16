from django.shortcuts import render

# Create your views here.
class View():
    authentication_classes = [CustomAuthentication]
    permission_classes = [IsAuthenticated, IsAuthorized]
    request_user = None