from django.urls import path, include
from .import views

urlpatterns = [
    path("sendmail/", views.send_mail, name='send_mail'),

]