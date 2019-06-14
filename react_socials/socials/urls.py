from rest_framework import routers
from .api import SocialsViewSet

router = routers.DefaultRouter()
router.register('api/socials', SocialsViewSet, 'user')

urlpatterns = router.urls