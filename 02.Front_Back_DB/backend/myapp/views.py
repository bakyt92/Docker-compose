from django.shortcuts import render
from django.db import connection
# Create your views here.


def index(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT version();")
        db_version = cursor.fetchone()
    return render(request, 'myapp/index.html', {'db_version': db_version[0]})

# from django.shortcuts import render
# from django.http import HttpResponse
# from django.db import connection
# # Create your views here.


# def index(request):
#     with connection.cursor() as cursor:
#         cursor.execute("SELECT version();")
#         db_version = cursor.fetchone()
#     return HttpResponse(f"Привет из Django! :), и база данных: {db_version[0]}")