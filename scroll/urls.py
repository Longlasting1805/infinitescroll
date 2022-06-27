from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserPostView

router = DefaultRouter()
router.register('userposts', UserPostView, basename='blogposts')

urlpatterns = [
    path('', include(router.urls)),
    # path('blogposts/', BlogView.as_view())
]