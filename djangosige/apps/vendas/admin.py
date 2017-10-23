from django.contrib import admin
from .models import Pagamento, Cheque, Cartao, Maquineta, Prospect

admin.site.register(Pagamento)
admin.site.register(Cheque)
admin.site.register(Cartao)
admin.site.register(Maquineta)
admin.site.register(Prospect)
