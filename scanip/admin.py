from django.contrib import admin
from .models import Dispositivo

@admin.register(Dispositivo)
class ScanipAdmin(admin.ModelAdmin):
    list_display = ['ip', 'nome']
    search_fields = ['ip', 'nome']
