from rest_framework import serializers
from ..models import Pedido

class PedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pedido
        fields = ['id', 'empresa_id', 'tipo', 'descricao', 'valor', 'data_submissao', 'estado']
 
   