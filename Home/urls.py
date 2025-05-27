from django.contrib import admin
from django.urls import path, include
from tu_app.views import home

urlpatterns = [
    path('', home, name='home'),
    path('productos/', include('productos.urls')),
    path('ventas/', include('ventas.urls')),
    path('compras/', include('compras.urls')),
    path('admin/', admin.site.urls),
]