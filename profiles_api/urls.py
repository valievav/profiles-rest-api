from django.urls import path, include
from rest_framework.routers import DefaultRouter

from profiles_api import views


# register viewsets in a router
router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, basename='hello-viewset')  # registered viewset in a new router
router.register('profile', views.UserProfileViewSet)  # basename is not specified since exists queryset in UserProfileViewSet

urlpatterns = [
    path('hello-view/', views.HelloAPIView.as_view()),
    path('login/', views.UserLoginApiView.as_view()),
    path('', include(router.urls)),  # generated urls to each viewset function
]
