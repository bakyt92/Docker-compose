from django.http import HttpResponse

def index(request):
    return HttpResponse("""
        <h1>Это приложение 3</h1>
        <a href="/">На главную</a>
    """)