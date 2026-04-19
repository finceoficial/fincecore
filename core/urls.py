from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/auth/", include("src.users.urls")),
    path("api/firms/", include("src.firms.urls")),
]
