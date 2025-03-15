from django.urls import path
from . import views

# Remove the app_name line to get rid of the namespace
# app_name = 'app'

urlpatterns = [
    path('test-template/', views.test_template, name='test_template'),
    path('khutbah/<int:khutbah_id>/', views.khutbah_detail, name='khutbah_detail'),
] 