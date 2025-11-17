
from django.urls import path
from greeting import views

urlpatterns = [
    path('', views.gallery),
    path('contact/', views.contact)
    
]
