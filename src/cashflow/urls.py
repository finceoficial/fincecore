from rest_framework.routers import DefaultRouter
from src.cashflow.views.cashflow import CashflowViewSet

router = DefaultRouter()
router.register("", CashflowViewSet, basename="cashflow")

urlpatterns = router.urls