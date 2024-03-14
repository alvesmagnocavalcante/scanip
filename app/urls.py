from django.urls import path
from django.contrib import admin
from scanip.views import ScanNetworkView, AdicionarDispositivoView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ScanNetworkView.as_view(), name='scan_network'),
    path('adicionar-dispositivo/', AdicionarDispositivoView.as_view(), name='adicionar_dispositivo'),
]