from django.urls import path
from .views import register_form, login_view, logout_view

urlpatterns = [
    path('register/', register_form, name='register_form_urls'),
    path('login/', login_view, name='login_user_urls'),
    path('logout/', logout_view, name='logout_user_urls'),
]