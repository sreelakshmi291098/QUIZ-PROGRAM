from rest_framework import serializers
from . models import login,stud_Reg,Question

class LoginStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=login
        fields="__all__"

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=stud_Reg
        fields="__all__"
    
    def Create(self,validated_data):
        return stud_Reg.object.create(**validated_data)

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model=Question
        fields="__all__"
    
    def Create(self,validated_data):
        return Question.object.create(**validated_data)