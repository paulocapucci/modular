from django.urls import path

from exemplo import views

app_name = 'exemplo'

urlspatterns = [
    path('list', views.ClienteList.as_view(), name='exemplo_list')
]