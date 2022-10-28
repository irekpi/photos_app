from rest_framework import routers
from app.views import PhotoViewSet, ExternalPhotoViewSet

router = routers.DefaultRouter()
router.register(r'photos', PhotoViewSet, basename='photos')
router.register(r'external', ExternalPhotoViewSet, basename='external')
