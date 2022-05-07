from django.shortcuts import render

# Create your views here.
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from aplv.models import Aplv
from aplv.serializers import AplvSerializer
from rest_framework.decorators import api_view

@api_view(['GET', 'POST', 'DELETE'])
def aplv_list(request):
    if request.method == 'GET':
        aplv = Aplv.objects.all()
        
        title = request.GET.get('title', None)
        if title is not None:
            aplv = aplv.filter(title__icontains=title)
        
        aplv_serializer = AplvSerializer(aplv, many=True)
        return JsonResponse(aplv_serializer.data, safe=False)
        # 'safe=False' for objects serialization
 
    elif request.method == 'POST':
        aplv_data = JSONParser().parse(request)
        aplv_serializer = AplvSerializer(data=aplv_data)
        if aplv_serializer.is_valid():
            aplv_serializer.save()
            return JsonResponse(aplv_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(aplv_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = Aplv.objects.all().delete()
        return JsonResponse({'message': '{} Cadastro deletado com sucesso!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'PUT', 'DELETE'])
def getbyid(request, id):
    try: 
        aplv = Aplv.objects.get(id=id) 
    except Aplv.DoesNotExist: 
        return JsonResponse({'message': 'O cadastro não existe!'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        aplv_serializer = AplvSerializer(aplv) 
        return JsonResponse(aplv_serializer.data) 
 
    elif request.method == 'PUT': 
        aplv_data = JSONParser().parse(request) 
        aplv_serializer = AplvSerializer(aplv, data=aplv_data) 
        if aplv_serializer.is_valid(): 
            aplv_serializer.save() 
            return JsonResponse(aplv_serializer.data) 
        return JsonResponse(aplv_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        aplv.delete() 
        return JsonResponse({'message': 'Cadastro deletado com sucesso!'}, status=status.HTTP_204_NO_CONTENT)

