from rest_framework.routers import DefaultRouter
from src.expenses.views.expenses import ExpenseViewSet

router = DefaultRouter()
router.register("", ExpenseViewSet, basename="expenses")

urlpatterns = router.urls