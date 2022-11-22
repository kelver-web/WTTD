from django.urls import path
from . import views

app_name = 'subscription'

urlpatterns = [
    path('', views.new, name='new'),
    path('<int:pk>/', views.detail, name='detail'),

]