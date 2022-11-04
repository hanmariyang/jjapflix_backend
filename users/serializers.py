from rest_framework import serializers
from users.models import User
from dj_rest_auth.registration.serializers import RegisterSerializer


class customRegistrationSerializer(RegisterSerializer):  # dj-rest-auth 회원가입 시리얼라이저
    
    nickname = serializers.CharField(max_length=20)
    
    def get_cleaned_data(self):
        data = super().get_cleaned_data()
        data['nickname'] = self.validated_data.get('nickname', '')

        return data
   
class UserProfileSerializer(serializers.ModelSerializer):  # 프로필 조회
    class Meta:
        model = User
        fields="__all__"



class UserUpdateSerializer(serializers.ModelSerializer):  # 닉네임 변경
    class Meta:
        model = User
        fields=("nickname",)
        
    def update(self, instance, validated_data): # 비밀번호 수정 
        for key, value in validated_data.items():
            if key == "password":
                instance.set_password(value)
                continue
            setattr(instance, key, value)
            
        instance.save()
        
        return instance