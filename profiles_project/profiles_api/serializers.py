from rest_framework import serializers
from profiles_api import models 

class HelloSerializer(serializers.Serializer):
    """ Serializa un campo para probar nuestra APIView """
    name = serializers.CharField(max_length=10)
    
class UserProfileSerializer(serializers.ModelSerializer):
    """ Serializa objeto de perfil de usuario """
    
    class Meta:
        model = models.UserProfile
        fields = ('id', 'email', 'name', 'password')
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {'imput_type': 'password'}
            }
        }
    
    def create(self, validated_data):
        """ Crear y validar nuevo usuario """