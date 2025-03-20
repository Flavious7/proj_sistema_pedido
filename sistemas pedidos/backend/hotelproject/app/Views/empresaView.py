from django.shortcuts import render
from django.http import JsonResponse
from ..models import Empresa
from ..Serializers.empresaSerializer import EmpresaSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET'])
def empresa_list(request):
    if request.method == 'GET':
        empresa = Empresa.objects.all()
        serializer = EmpresaSerializer(empresa, many=True)
        return JsonResponse(serializer.data, safe=False)


@api_view(['GET'])
def empresa_get(request, id):
    try:
        empresa = Empresa.objects.get(id= id)
    except Empresa.DoesNotExist:
        empresa={}
        return JsonResponse({"message": "Empresa not found."}, status=status.HTTP_208_ALREADY_REPORTED)    
        
    if request.method == 'GET':
        serializer = EmpresaSerializer(empresa)
        return JsonResponse(serializer.data, safe=False)

@api_view(['POST'])
def empresa_create(request):
    if request.method == 'POST':
        email = request.data.get('email')
        if Empresa.objects.filter(email=email).exists():
            return Response({"error": "A client with this email already exists."}, status=status.HTTP_401_UNAUTHORIZED)
        serializer = EmpresaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
 
    
# @api_view(['POST'])
# def empresa_create(request):
#     if request.method == 'POST':
#         serializer = EmpresaSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status = status.HTTP_201_CREATED)
        
        
@api_view(['PUT'])
def empresa_update(request, id):
    try:
        empresa = Empresa.objects.get(id= id)
    except Empresa.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'PUT':
        serializer = EmpresaSerializer(empresa, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_200_OK)
        
        return Response(serializer.data, status = status.HTTP_400_BAD_REQUEST)
        
@api_view(['DELETE'])
def empresa_delete(request, id):
    try:
        empresa = Empresa.objects.get(id=id)
    except Empresa.DoesNotExist:
        return JsonResponse({"message": "Empresa not found."}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'DELETE':
        empresa.delete()
        return JsonResponse({"message": "Empresa deleted successfully"}, status=status.HTTP_200_OK)

