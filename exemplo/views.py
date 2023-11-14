from django.views.generic import ListView
from exemplo.models import Cliente

class ClienteList(ListaView):
    model = Cliente
    queryset = Cliente.objects.all()