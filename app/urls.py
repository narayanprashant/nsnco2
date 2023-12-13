from django.urls import path
from app.views import generate_product_description, image_recognition

urlpatterns = [
    path('generate_description/', generate_product_description, name='generate_product_description'),
    path('image_recognition/', image_recognition, name='image_recognition'),
]
