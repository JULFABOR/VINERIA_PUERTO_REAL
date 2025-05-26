from django.urls import path, include
from APERTURA_CAJA import views

urlpatterns = [
    path('',views.index, name='index'),
]