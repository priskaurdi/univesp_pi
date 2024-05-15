from django.urls import path 
from myapp import views

urlpatterns = [
    path('', views.home, name='home'),
    path('list-item', views.list_item, name='list-item'),
    path('form-reservation/<int:id>/', views.form_reservation, name='reservation-create'),
    path('form-appointment/', views.form_appointment, name='appointment-create'),    
    path('home/', views.home, name='home'),
    # Versão 02-05-2024
    #path('reservation-create/<int:id>/', views.reservation_create, name='reservation-create'),
 ]