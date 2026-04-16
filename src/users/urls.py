from django.urls import path
from .views.register import (
    RegisterView,
)

from .views.login import (
    LoginView
)

from .views.reset_password import (
    RequestPasswordResetView,
    ConfirmPasswordResetView
)

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),
    path('password-reset/', RequestPasswordResetView.as_view()),
    path('password-reset-confirm/', ConfirmPasswordResetView.as_view()),
]