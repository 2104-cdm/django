from . import views
from django.urls import path

urlpatterns = [
    path('entrada', views.entrada, name='entrada'),
    path('usando_create', views.usando_create, name='usando_create'),
    path('usando_save', views.usando_save, name='usando_save'),
    # path('salida/', views.salida, name='salida'),
]
