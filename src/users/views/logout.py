from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken


class LogoutView(APIView):
    def post(self, request):
        try:
            refresh_token = request.data.get("refresh")
            token = RefreshToken(refresh_token)
            token.blacklist()

            return Response({"detail": "Logout realizado com sucesso"})
        except Exception:
            return Response({"detail": "Token inválido"}, status=status.HTTP_400_BAD_REQUEST)