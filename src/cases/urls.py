from rest_framework.routers import DefaultRouter
from ..cases.views.case import CaseViewSet

router = DefaultRouter()
router.register("", CaseViewSet, basename="cases")

urlpatterns = router.urls