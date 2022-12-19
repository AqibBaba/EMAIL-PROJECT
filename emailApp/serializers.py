from rest_framework import serializers
from .models import User,AuthTokens

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields='__all__'


class TokenSerializer(serializers.ModelSerializer):
    class Meta:
        model=AuthTokens
        fields=['user_id','isExpired','token']

class UserVMSerializer1(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['username','password', 'firstname','lastname','email']
    


