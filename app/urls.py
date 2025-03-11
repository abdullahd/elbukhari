from django.urls import path
from . import views

urlpatterns = [
    path('test-template/', views.test_template, name='test_template'),
] 