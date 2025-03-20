from django.shortcuts import render
from django.http import JsonResponse
from ..models import Pedido
from ..Serializers.pedidoSerializer import PedidoSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import requests

@api_view(['GET'])
def pedido_list(request):
    
    if request.method == 'GET':
        pedidos = Pedido.objects.all()
        serializer = PedidoSerializer(pedidos, many=True)
        return JsonResponse(serializer.data, safe=False)


@api_view(['GET'])
def pedido_get(request, id):
    try:
        pedido = Pedido.objects.get(id= id)
    except Pedido.DoesNotExist:
        pedido={}
        return JsonResponse({"message": "Pedido not found."}, status=status.HTTP_208_ALREADY_REPORTED)    
        
    if request.method == 'GET':
        serializer = PedidoSerializer(pedido)
        return JsonResponse(serializer.data, safe=False)

@api_view(['POST'])
def pedido_create(request):
    
    if request.method == 'POST':
        data = request.data.copy()
        data['estado'] = 'pendente'

        serializer = PedidoSerializer(data=data)
        
        if serializer.is_valid():
            pedido = serializer.save()
            
            # Chamar WSO2
            wso2_url = "http://wso2mi:8290/validarpedido"
            payload = {
                "pedido_id": pedido.id,
                "valor": pedido.valor
            }
            try:
                print("im here")
                wso2_resp = requests.post(wso2_url, json=payload)
                # Exemplo: se wso2_resp.json() == {"validacaoExterna":"ok"}
                # então aplicar a regra de <1000 => APROVAR, senão REJEITAR
                if wso2_resp.status_code == 200:
                    resp_data = wso2_resp.json()
                    # digamos que resp_data["validacaoExterna"] == "ok"
                    if resp_data.get("validacaoExterna") == "ok":
                        # agora aplica a regra do valor
                        if pedido.valor < 1000:
                            pedido.estado = "APROVADO"
                        else:
                            pedido.estado = "PENDENTE"  # ou "AGUARDANDO_APROVACAO"
                        pedido.save()
                    else:
                        pedido.estado = "REJEITADO"
                        pedido.save()
                else:
                    # Se wso2 nao respondeu 200, talvez manter pendente ou rejeitar
                    print("WSO2 não respondeu OK. Status:", wso2_resp.status_code)
            except Exception as e:
                print("Erro ao chamar WSO2:", e)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                # Decide se retorna erro ou ignora. Depende do seu projeto.

            # Retornar a versão final do pedido (já com o estado atualizado)
            return Response(PedidoSerializer(pedido).data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        
 
    
# @api_view(['POST'])
# def pedido_create(request):
#     if request.method == 'POST':
#         serializer = PedidoSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status = status.HTTP_201_CREATED)
        
        
@api_view(['PUT'])
def pedido_update(request, id):
    try:
        pedido = Pedido.objects.get(id= id)
    except Pedido.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'PUT':
        serializer = PedidoSerializer(pedido, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_200_OK)
        
        return Response(serializer.data, status = status.HTTP_400_BAD_REQUEST)
        
@api_view(['DELETE'])
def pedido_delete(request, id):
    try:
        pedido = Pedido.objects.get(id=id)
    except Pedido.DoesNotExist:
        return JsonResponse({"message": "Pedido not found."}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'DELETE':
        pedido.delete()
        return JsonResponse({"message": "Pedido deleted successfully"}, status=status.HTTP_200_OK)

