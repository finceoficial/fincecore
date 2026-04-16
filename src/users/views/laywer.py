from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from ..models.laywer import LawyerProfile
from ..serializers.laywer import LawyerProfileUpdateSerializer


class LawyerProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = LawyerProfileUpdateSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user.profile