from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_redister, name='register'),
    path('login', views.login_view, name='login'),
    path('sucess', views.sucess_view, name='sucess'),
    path('logout', views.logout_view, name='logout'),
]
