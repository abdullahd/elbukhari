from django.urls import path
from . import views

urlpatterns = [
    path('newsletter/subscribe/', views.newsletter_subscribe, name='newsletter_subscribe'),
    path('newsletter/success/', views.newsletter_success, name='newsletter_success'),
    path('newsletter/confirm/<str:token>/', views.newsletter_confirm, name='newsletter_confirm'),
    path('newsletter/confirmed/', views.newsletter_confirmed, name='newsletter_confirmed'),
    path('newsletter/unsubscribe/<str:email_encoded>/', views.newsletter_unsubscribe, name='newsletter_unsubscribe'),
    path('newsletter/unsubscribed/', views.newsletter_unsubscribed, name='newsletter_unsubscribed'),
] 