from django.urls import path
from exemplo import views
from exemplo.views import ClienteCreate

app_name = 'exemplo'

urlpatterns = [
    path('', views.ClienteList.as_view(), name='list'),
    path('create/', views.ClienteCreate.as_view(), name='create'),
    path('update/<int:pk>/', views.ClienteUpdate.as_view(), name='update'),
    path('delete/<int:pk>/', views.ClienteDelete.as_view(), name='delete'),
    path('detail/<int:pk>/', views.ClienteDetail.as_view(), name='detail'),
]