from rest_framework.generics import ListCreateAPIView
from .models import CustomUser
from .serializers import CustomUserSerializer

class UserListCreateView(ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

class UserSearchView(ListCreateAPIView):
    serializer_class = CustomUserSerializer

    def get_queryset(self):
        first_name = self.request.query_params.get('first_name', '')
        last_name = self.request.query_params.get('last_name', '')
        queryset = CustomUser.objects.filter(first_name__icontains=first_name, last_name__icontains=last_name)
        return queryset
