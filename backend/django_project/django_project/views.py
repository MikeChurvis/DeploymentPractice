import os
from django.http import JsonResponse

def say_hello(request):
    return JsonResponse({ "quoth the config file": os.environ.get('HELLO_WORLD')})