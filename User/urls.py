from django.urls import path
from .views import login_view, register_view, account_user_view


app_name = 'User'

urlpatterns = [
    path('', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('account/', account_user_view, name='account')
]