from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse

@csrf_exempt
def index(request):
    if request.method == 'GET':
        response = JsonResponse({'req_method' : 'GET'}, status = 200)
        return response
    elif request.method == 'POST':
        response = JsonResponse({'req_method' : 'POST'}, status = 200)
        return response
    else:
        response = JsonResponse({'error': 'request method not allowed'}, status = 400)
        return response