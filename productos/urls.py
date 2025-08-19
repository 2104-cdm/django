from . import views
from django.urls import path

urlpatterns = [
    path('entrada', views.entrada, name='entrada'),
    # path('salida/', views.salida, name='salida'),
]
