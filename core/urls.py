from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('palestrantes/<slug:slug>/', views.speaker_detail, name='speaker_detail'),
    path('palestras/', views.talk_list, name='talk_list'),
]
