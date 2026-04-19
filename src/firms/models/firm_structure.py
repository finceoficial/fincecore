from django.db import models

class Firm(models.Model):
    class FirmType(models.TextChoices):
        SOLO = "SOLO"
        OFFICE = "OFFICE"

    name = models.CharField(max_length=255)
    type = models.CharField(max_length=20, choices=FirmType.choices)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
