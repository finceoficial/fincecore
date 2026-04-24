from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response

from src.cashflow.services.cashflow_manipulation import CashflowService


class CashflowViewSet(viewsets.ViewSet):
    permission_classes = [permissions.IsAuthenticated]

    def get_firm(self, request):
        return request.user.firm_memberships.first().firm

    @action(detail=False, methods=["get"])
    def projection(self, request):
        firm = self.get_firm(request)

        days = int(request.query_params.get("days", 60))

        data = CashflowService.get_projection(firm, days)

        return Response(data)

    @action(detail=False, methods=["get"])
    def summary(self, request):
        firm = self.get_firm(request)

        data = CashflowService.get_summary(firm)

        return Response(data)