from rest_framework import serializers
from .models import *


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

