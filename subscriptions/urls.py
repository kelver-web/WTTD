from django.urls import path
from . import views

urlpatterns = [
    path('', views.subscription),
    path('<int:pk>/', views.detail, name='detail'),

]