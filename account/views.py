from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_POST
from rest_framework.permissions import AllowAny,IsAuthenticated
#from common.decorators import ajax_required
#from actions.utils import create_action
#from actions.models import Action
from .models import Profile
from .permissions import IsOwnerOrReadOnly
from django.contrib.auth import get_user_model
from rest_framework import viewsets
from .serializers import ProfileSerializer
from rest_framework.generics import (ListCreateAPIView,RetrieveUpdateDestroyAPIView,)
import os
from datetime import timedelta
from importlib import import_module
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.contrib import auth
from django.template.loader import render_to_string
from django.utils.decorators import method_decorator
from django.utils.timezone import now
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.reverse import reverse
from django.http import JsonResponse

from rest_framework import mixins
from rest_framework import generics

from rest_framework.views import APIView
#from images.models import Image
#from images.serializers import ImageSerializer





class ProfileViewSet(viewsets.ModelViewSet):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()

    
 
    def perform_create(self, serializer):
        user=self.request.user
        serializer =serializer.save(user=user)

        
    def get_permissions(self):        
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        if self.action == 'create' or self.action == 'update' or self.action == 'partial_update' or self.action == 'destroy':
            permission_classes = [IsOwnerOrReadOnly,IsAuthenticated]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]
    
   
    
