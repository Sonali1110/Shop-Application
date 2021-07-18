from django.conf.urls import url
from . import views

app_name = 'orders'

urlpatterns = [
    url('create/$', views.order_create, name='order_create'),
    url('created/$', views.order_create, name='order_create'),
]