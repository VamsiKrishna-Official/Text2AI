from django.urls import path
from .views import ClassAI

urlpatterns = [
    path('input/', ClassAI.as_view(), name='input')
]