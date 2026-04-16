from django.contrib import admin

from .models import User, LawyerProfile

admin.site.register(User)
admin.site.register(LawyerProfile)
