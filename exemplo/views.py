from django.views.generic import ListView
from exemplo.models import Cliente

class ClienteList(ListView):
    model = Cliente
    queryset = Cliente.objects.all()