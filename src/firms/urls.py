from rest_framework.routers import DefaultRouter
from ..firms.views.firm import FirmViewSet

router = DefaultRouter()
router.register("", FirmViewSet, basename="firms")

urlpatterns = router.urls