from django.http import HttpResponse

def index(request):
    return HttpResponse("""
        <h1>Это приложение 0</h1>
        <a href="/app1">На app1</a>
        <a href="/app2">На app2</a>
        <a href="/app3">На app3</a>
    """)