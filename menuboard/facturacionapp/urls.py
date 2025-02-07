from django.urls import path

from estadisticas import views
from .views import *
app_name = 'facturacion'
urlpatterns = [
    path('checkout/', views.checkout, name='checkout'),
    path('index/',views.index),
    path('',views.home, name='home_facturacion'),

]