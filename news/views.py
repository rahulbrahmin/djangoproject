from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def get_news(request):
    if request.method == "POST":
        data = {
            "response" : "Bits News Django App"
        }
        return JsonResponse(data)
    return HttpResponse("Hello World")