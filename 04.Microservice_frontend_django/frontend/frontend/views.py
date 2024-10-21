from django.http import HttpResponse
import requests

def index(request):
    return HttpResponse("""
        <h1>Главная страница</h1>
        <a href="/app1/">Приложение 1</a><br>
        <a href="/app2/">Приложение 2</a><br>
        <a href="/app3/">Приложение 3</a>
    """)

def app1_view(request):
    response = requests.get('http://app1:8001/')
    data = response.json()
    return HttpResponse(f"<h1>{data['message']}</h1><a href='/'>На главную</a>")

def app2_view(request):
    response = requests.get('http://app2:8002/')
    data = response.json()
    return HttpResponse(f"<h1>{data['message']}</h1><a href='/'>На главную</a>")

def app3_view(request):
    response = requests.get('http://app3:8003/')
    data = response.json()
    return HttpResponse(f"<h1>{data['message']}</h1><a href='/'>На главную</a>")