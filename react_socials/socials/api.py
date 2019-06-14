from .models import User
from rest_framework import viewsets, permissions
from .serializers import SocialsSerializer

class SocialsViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]

    serializer_class = SocialsSerializer