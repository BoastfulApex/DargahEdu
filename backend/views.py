from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import *


class SliderView(ModelViewSet):
    queryset = Slider.objects.all() 
    serializer_class = SliderSerializer


class CourceView(ModelViewSet):
    queryset = Cource.objects.all() 
    serializer_class = CourceSerializer


class CommentView(ModelViewSet):
    queryset = Comment.objects.all() 
    serializer_class = CommentSerializer


class FAQView(ModelViewSet):
    queryset = FAQ.objects.all() 
    serializer_class = FAQSerializer


class TeacherView(ModelViewSet):
    queryset = Teacher.objects.all() 
    serializer_class = TeacherSerializer
