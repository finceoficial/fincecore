from django.db import models

from src.firms.models.firm_structure import Firm

class FirmMember(models.Model):
    class Role(models.TextChoices):
        OWNER = "OWNER"
        LAWYER = "LAWYER"
        STAFF = "STAFF"

    firm = models.ForeignKey(Firm, on_delete=models.CASCADE, related_name="members")
    user = models.ForeignKey("users.User", on_delete=models.CASCADE, related_name="firm_memberships")
    role = models.CharField(max_length=20, choices=Role.choices)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("firm", "user")
    def __str__(self):
        return f"{self.user.username} - {self.firm.name} ({self.role})"
