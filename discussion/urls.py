from discussion.models import QA
from django.urls import path, include
from django.contrib.auth import views as auth_views


from rest_framework import routers, serializers, viewsets
from django.views.decorators.csrf import csrf_exempt
from rest_framework.routers import DefaultRouter
from .views import QAViewSet,AnswerViewSet

app_name = 'discussion'

router = DefaultRouter()
router.register(r'questions', QAViewSet)
router.register(r'answers', AnswerViewSet)


urlpatterns = [

   path('', include(router.urls)),

#    path('timeline/', ActionDetail.as_view()),

  

]
