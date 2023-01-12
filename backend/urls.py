from django.urls import path, include
from .views import LoginView, ConfirmView

urlpatterns = [
    path('login/', LoginView.as_view()),
    path('confirm_phone/', ConfirmView.as_view()),
]
