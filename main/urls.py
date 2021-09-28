from django.urls import path
from . import views

app_name = 'main'
urlpatterns = [
    path('', views.index, name='index'),
    path('mail/send/', views.mail_send, name='mail_send')
]