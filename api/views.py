from rest_framework.generics import ListAPIView
from django.contrib.auth.models import User

from api.serializers import UserSerializer
# Create your views here.

class TestApiView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer