from django.shortcuts import render
from .serializers import *
from rest_framework import generics, viewsets
from functions import send_sms, get_click_url, get_payme_url
import random
from rest_framework.response import Response
from data import config
from rest_framework.permissions import AllowAny, IsAuthenticated


def generateOTP():
    return random.randint(111111, 999999)


class SliderView(viewsets.ModelViewSet):
    queryset = Slider.objects.all() 
    serializer_class = SliderSerializer


class CourceView(viewsets.ModelViewSet):
    queryset = Cource.objects.all() 
    serializer_class = CourceSerializer


class CommentView(viewsets.ModelViewSet):
    queryset = Comment.objects.all() 
    serializer_class = CommentSerializer


class FAQView(viewsets.ModelViewSet):
    queryset = FAQ.objects.all() 
    serializer_class = FAQSerializer


class TeacherView(viewsets.ModelViewSet):
    queryset = Teacher.objects.all() 
    serializer_class = TeacherSerializer


class LoginView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = LoginSerializer

    def create(self, request, *args, **kwargs):
        name = request.data['name']
        phone = request.data['phone']
        otp = generateOTP()
        user, created = User.objects.get_or_create(
            phone=phone
        )
        user.name = name
        user.otp = otp
        print(otp)
        user.save()
        send_sms(phone=phone, otp=otp)
        return Response({"status": "created"})


class ConfirmView(generics.CreateAPIView):
    queryset = User.objects.all() 
    permission_classes = (AllowAny,)
    serializer_class = ConfirmSerializer

    def create(self, request, *args, **kwargs):
        phone = request.data['phone']
        otp = request.data['otp']
        pay_type = request.data['pay_type']
        user = User.objects.filter(phone=phone).first()
        cource = Cource.objects.all()[0]
        if user.otp ==  otp:   
            succes = f"https://t.me/dargah_edu_bot?start={user.phone}"
            if pay_type == "payme":
                url = get_payme_url(succes_url=succes, user_id=user.id)
                return Response({"url": url})
            if pay_type == "click":
                url = get_click_url(service_id=config.CLICK_SERVICE_ID, merchant_id=config.CLICK_MERCHANT_ID, return_url=succes, amount=1000, transaction_id=config.CLICK_MERCHANT_USER_ID)
                return Response({"url": url})
        else:
            return Response({"status": "ERROR"})
                
