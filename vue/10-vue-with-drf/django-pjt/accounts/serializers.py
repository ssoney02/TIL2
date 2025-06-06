# accounts/serializers.py

from dj_rest_auth.registration.serializers import RegisterSerializer
from rest_framework import serializers

class CustomRegisterSerializer(RegisterSerializer):
    age = serializers.IntegerField(required=True)
    
    def get_cleaned_data(self):
        data = super().get_cleaned_data()
        # 원래 있던 get_cleaned_data는 덮어씌워지면 안됨!!
        data['age'] = self.validated_data.get('age', '')
        return data
    
    def save(self, request):
        user = super().save(request)
        user.age = self.validated_data.get('age','')
        user.save()
        return user