from django.urls import path, include
from .views import signup, profile_view

urlpatterns = [
    path('accounts/', include('allauth.urls')),  # URLs для django-allauth
    path('signup/', signup, name='signup'),
    path('accounts/profile/', profile_view, name='profile'),  # URL для профиля
]
