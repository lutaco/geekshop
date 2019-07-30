from django.urls import path
from .views import registration_view
from django.contrib.auth.views import LoginView

app_name = 'accounts'

urlpatterns = [
    path('', LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('registration', registration_view, name='registration'),
]
