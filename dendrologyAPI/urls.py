from django.urls import path
from .views import *

urlpatterns = [
    path('dendrology/', TreeCreate.as_view()),
]
