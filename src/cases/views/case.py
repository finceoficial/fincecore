from rest_framework import viewsets, permissions
from ..models.case_structure import Case
from ..serializers.case import CaseSerializer


class CaseViewSet(viewsets.ModelViewSet):
    serializer_class = CaseSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Case.objects.filter(
            firm__members__user=self.request.user
        )

    def perform_create(self, serializer):
        firm = self.request.user.firm_memberships.first().firm
        serializer.save(firm=firm)