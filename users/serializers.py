from django.core.mail import send_mail
from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'first_name',
            'last_name'
        )

class CreateUserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    #Se hashea la contraseña antes de guardarse en la bd
    def create(self, validated_data):
        user = User(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )
        user.set_password(validated_data['password'])
        user.save()
        """        send_mail(
            'Asunto',
            'Cuerpo',
            'hola@gmail.com',
            [validated_data['email']],
            fail_silently=False,
        )"""
        return user

