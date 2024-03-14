from django.shortcuts import render, redirect
from django.views.generic import TemplateView, CreateView
from django.urls import reverse_lazy
from .forms import DispositivoForm
from .models import Dispositivo
from scapy.all import ARP, Ether, srp

def scan_network(ip_range):
    # Cria um pacote ARP solicitando todos os IPs no range especificado
    arp = ARP(pdst=ip_range)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether / arp

    # Envia o pacote ARP e recebe as respostas
    result = srp(packet, timeout=3, verbose=False)[0]

    # Extrai os IPs e MACs das respostas
    devices = []
    for sent, received in result:
        devices.append({'ip': received.psrc, 'mac': received.hwsrc})

    return devices

class ScanNetworkView(TemplateView):
    template_name = 'scan_network.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        devices = scan_network("192.168.42.0/24")  # Chamando a função scan_network
        dispositivos_conhecidos = Dispositivo.objects.all()

        for device in devices:
            dispositivo_existente = dispositivos_conhecidos.filter(ip=device['ip']).first()
            if dispositivo_existente:
                device['nome'] = dispositivo_existente.nome
            else:
                device['nome'] = "Desconhecido"

        context['devices'] = devices
        return context

class AdicionarDispositivoView(CreateView):
    template_name = 'adicionar_dispositivo.html'
    form_class = DispositivoForm
    success_url = reverse_lazy('scan_network')

    def form_valid(self, form):
        form.save()
        return redirect(self.success_url)