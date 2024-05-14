from django.urls import path,include
from rest_framework import routers
from . import views
from .views import index

app_name = 'src'

router=routers.DefaultRouter()
router.register(r'programmers',views.ProgrammerViewSet)

urlpatterns=[
    path('', include(router.urls)),
    path('index/', index, name='index'),
    path('registro/', views.registro, name='registro'),
    path('soporte/', views.soporte, name='soporte'),
    path('convertidor/', views.convertidor, name='convertidor'),
    path('iniciarsesion/', views.iniciarsesion, name='iniciarsesion'),
    path('add/<int:product_id>/', views.agregar_producto, name="add"),
]