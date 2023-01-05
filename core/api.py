from rest_framework import routers
from backend.views import *

router = routers.DefaultRouter()

router.register(r"sliders", SliderView, basename="sliders")
router.register(r"cources", SliderView, basename="cources")
router.register(r"comments", SliderView, basename="comments")
router.register(r"teachers", SliderView, basename="teachers")
router.register(r"faq", SliderView, basename="faq")