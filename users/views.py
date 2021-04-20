
from rest_framework.viewsets import ModelViewSet
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny
from users.serializers import CreateUserSerializer, UserSerializer

class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    #permission_classes = (AllowAny,)

    def get_serializer_class(self):
        if self.request.method == 'POST':

            return CreateUserSerializer
        return UserSerializer

    def get_permissions(self):
        if self.request.method == 'POST':
            self.permission_classes = (AllowAny, )
            #return [p() for p in (AllowAny, )]

        return super(UserViewSet, self).get_permissions()