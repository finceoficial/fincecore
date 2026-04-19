from ..models.firm_member import FirmMember
from ..models.firm_structure import Firm
from ..serializers.firm import FirmSerializer, FirmCreateSerializer, FirmMemberSerializer

from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response

class FirmViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Firm.objects.filter(members__user=self.request.user)

    def get_serializer_class(self):
        if self.action == "create":
            return FirmCreateSerializer
        return FirmSerializer

    @action(detail=True, methods=["get"])
    def members(self, request, pk=None):
        members = FirmMember.objects.filter(
            firm_id=pk,
            firm__members__user=request.user
        )
        serializer = FirmMemberSerializer(members, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=["post"])
    def add_member(self, request, pk=None):
        serializer = FirmMemberSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        serializer.save(firm_id=pk)

        return Response(serializer.data)