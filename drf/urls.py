from django.contrib import admin
from django.urls import path, include
from rest_framework.documentation import include_docs_urls
from src import views as src_views


urlpatterns = [
    path('', src_views.index, name='index'),
    path('admin/', admin.site.urls),
    path('src/', include('src.urls', namespace='src')),
    path('docs/', include_docs_urls(title='Documentation')),
    path('logout/', src_views.custom_logout, name='logout'),
    path('iniciarsesion/', src_views.iniciarsesion, name='iniciarsesion'),
    path('add/<int:product_id>/', src_views.agregar_producto, name="add"),
    path('remove/<int:product_id>/', src_views.eliminar_producto, name="remove"),
    path('restar/<int:product_id>/', src_views.restar_producto, name="restar"),
    path('limpiar/', src_views.limpiar_carrito, name="limpiar"),
    path('checkout/<int:product_id>/', src_views.CheckOut, name='checkout'),
    path('payment-success/<int:product_id>/', src_views.PaymentSuccessful, name='payment-success'),
    path('payment-failed/<int:product_id>/', src_views.paymentFailed, name='payment-failed'),
    path('', include('paypal.standard.ipn.urls')),
]
