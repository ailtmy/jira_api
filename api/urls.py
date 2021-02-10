from django.urls import path, include
from rest_framework import routers
from .views import TaskViewSet, CatagoryViewSet, CreateUserView, ListUserView, LoginUserView, ProfileViewSet

router = routers.DefaultRouter()
router.register('category', CatagoryViewSet)
router.register('tasks', TaskViewSet)
router.register('profile', ProfileViewSet)

urlpatterns = [
    path('create/', CreateUserView.as_view(), name='create'),
    path('users/', ListUserView.as_view(), name="users"),
    path('loginuser/', LoginUserView.as_view(), name='loginuser'),
    path('', include(router.urls)),
]