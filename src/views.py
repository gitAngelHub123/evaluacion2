from rest_framework import viewsets
from .serializer import ProgrammerSerializer
from .models import Programmer, product
from django.shortcuts import render, redirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .forms import tareaform
from src.Carrito import Carrito
from django.conf import settings
import uuid
from paypal.standard.forms import PayPalPaymentsForm


class ProgrammerViewSet(viewsets.ModelViewSet):
    queryset = Programmer.objects.all()
    serializer_class = ProgrammerSerializer

@login_required
def index(request):
    productoss = product.objects.all()
    carrito = Carrito(request)
    return render(request, 'src/index.html', {'productoss': productoss, 'carrito': carrito})

def agregar_producto(request, product_id):
    carrito = Carrito(request)
    productoss = product.objects.get(id=product_id)
    carrito.add(productoss)
    return redirect("src:index")

def eliminar_producto(request, product_id):
    carrito = Carrito(request)
    productoss = product.objects.get(id=product_id)
    carrito.remove(productoss)
    return redirect("src:index")

def restar_producto(request, product_id):
    carrito = Carrito(request)
    productoss = product.objects.get(id=product_id)
    carrito.restar(productoss)
    return redirect("src:index")

def limpiar_carrito(request):
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect("src:index")

def iniciarsesion(request):
    if request.method == 'GET':
        return render(request, 'src/iniciarsesion.html', {
            'form': AuthenticationForm
        })
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'src/iniciarsesion.html', {
                'form': AuthenticationForm,
                'error': 'Usuario o contraseña incorrectos'
            })
        else:
            login(request, user)
            return redirect(reverse('index'))

def redirigir_a_iniciarsesion(request):
    return redirect(reverse('iniciarsesion'))

def registro(request):
    if request.method == 'GET':
        form = UserCreationForm()
        return render(request, 'src/registro.html', {'form': form})
    elif request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            if form.cleaned_data['password1'] == form.cleaned_data['password2']:
                try:
                    user = User.objects.create_user(
                        username=form.cleaned_data['username'],
                        password=form.cleaned_data['password1'])
                    user.save()
                    login(request, user)
                    return redirect('index')
                except:
                    form.add_error(None, 'Error al crear el usuario. Inténtalo de nuevo.')
                    return render(request, 'src/registro.html', {'form': form})
            else:
                form.add_error('password2', 'Las contraseñas no coinciden')
                return render(request, 'src/registro.html', {'form': form})
        return render(request, 'src/registro.html', {'form': form})

def redirigir_a_registro(request):
    return redirect(reverse('registro'))

def convertidor(request):
    return render(request, 'src/convertidor.html')

def custom_logout(request):
    logout(request)
    return redirect('index') 

@login_required
def soporte(request):
    if request.method == 'GET': 
        return render(request, 'src/soporte.html', {
            'form': tareaform
        })
    else:
        try:
            form = tareaform(request.POST)
            nueva_tarea = form.save(commit=False)
            nueva_tarea.user = request.user
            nueva_tarea.save()
            return redirect('index')  # Redirigir al usuario al index.html
        except ValueError:
            return render(request, 'src/soporte.html', {
                'form': tareaform,
                'error': 'inserte algun dato'
                })
            
def CheckOut(request, product_id):
    productoss = product.objects.get(id=product_id)
    host = request.get_host()

    paypal_checkout = {
        'business': settings.PAYPAL_RECEIVER_EMAIL,
        'amount': productoss.price,
        'item_name': productoss.name,
        'invoice': uuid.uuid4(),
        'currency_code': 'USD',
        'notify_url': f"http://{host}{reverse('paypal-ipn')}/",
        'return_url': f"http://{host}{reverse('payment-success', kwargs={'product_id': productoss.id})}",
        'cancel_url': f"http://{host}{reverse('payment-failed', kwargs={'product_id': productoss.id})}",
    }

    paypal_payment = PayPalPaymentsForm(initial=paypal_checkout)

    context = {
        'productoss': productoss,
        'paypal': paypal_payment
    }

    return render(request, 'src/checkout.html', context)

def PaymentSuccessful(request, product_id):
    
    productoss = product.objects.get(id=product_id)

    return render(request, 'src/payment-success.html', {'productoss': productoss})

def paymentFailed(request, product_id):

    productoss = product.objects.get(id=product_id)

    return render(request, 'src/payment-failed.html', {'productoss': productoss})