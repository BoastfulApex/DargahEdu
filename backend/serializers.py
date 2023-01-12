from rest_framework import serializers
from .models import *
import re 


def isValid(s):
    Pattern = re.compile("(0|91)?[7-9][0-9]{9}")
    return Pattern.match(s)


class CourceSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Cource
        fields = "__all__"


class SliderSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Slider
        fields = "__all__"


class FAQSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = FAQ
        fields = "__all__"


class CommentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Comment
        fields = "__all__"


class TeacherSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Teacher
        fields = "__all__"


class LoginSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=200)
    phone = serializers.CharField(max_length=200)

    def validate(self, attrs):
        number = attrs['phone']

        if not isValid(number):
                    raise serializers.ValidationError({"phone": "Phone number isn't valid"})
        return attrs
    

class ConfirmSerializer(serializers.Serializer):
    phone = serializers.CharField(max_length=200)
    otp = serializers.CharField(max_length=200)
    pay_type = serializers.CharField(max_length=200)
    
