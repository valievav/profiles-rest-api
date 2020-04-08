from django.urls import path, include
from rest_framework.routers import DefaultRouter

from profiles_api import views


router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, basename='hello-viewset')  # registered viewset in a new router

urlpatterns = [
    path('hello-view/', views.HelloAPIView.as_view()),
    path('', include(router.urls))  # generated urls to each viewset function
]
