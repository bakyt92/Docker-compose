from django.http import HttpResponse

def index(request):
    return HttpResponse("""
        <h1>Это приложение 1</h1>
        <a href="/">На главную</a>
    """)