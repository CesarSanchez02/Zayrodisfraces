from datetime import date
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.conf import settings
from django.urls import reverse
from pages.models import Inventario, Categoria, Talla, Comentarios

import stripe
from django.views.decorators.csrf import csrf_exempt



@csrf_exempt
def products(request):
    inventarios = Inventario.objects.filter(id_disponibilidad__descripcion=True)
    categorias = Categoria.objects.all()
    tallas = Talla.objects.all()

    # Filtering
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')
    categoria = request.GET.get('categoria')
    talla = request.GET.get('talla')

    if min_price:
        inventarios = inventarios.filter(precio_unitario__gte=min_price)
    if max_price:
        inventarios = inventarios.filter(precio_unitario__lte=max_price)
    if categoria:
        inventarios = inventarios.filter(id_producto__id_categoria__categoria=categoria)
    if talla:
        inventarios = inventarios.filter(id_producto__id_talla__talla=talla)

    return render(request, "inicio/products.html", {'inventarios': inventarios, 'categorias': categorias, 'tallas': tallas})
@csrf_exempt
def inventario_detail(request, inventario_id):
    inventario = get_object_or_404(Inventario, id_inventario=inventario_id)
    comentarios = Comentarios.objects.filter(id_producto=inventario.id_producto)
    return render(request, 'inicio/inventario_detail.html', {'inventario': inventario, 'comentarios': comentarios})
@csrf_exempt
def checkout(request, inventario_id):
    inventario = Inventario.objects.get(id_inventario=inventario_id)
    if request.method == "POST":
        try:
            checkout_session = stripe.checkout.Session.create(
                payment_method_types=['card'],
                line_items=[{
                    'price': inventario.stripe_price_id,
                    'quantity': 1,
                }],
                mode='payment',
                success_url=request.build_absolute_uri(reverse('success')),
                cancel_url=request.build_absolute_uri(reverse('cancel')),
                locale='es',
            )
            return redirect(checkout_session.url)
        except stripe.error.StripeError as e:
            # Handle Stripe errors
            print(f"Stripe Error: {e}")
            return render(request, "checkout_error.html")

    return render(request, "checkout.html", {'inventario': inventario})
@csrf_exempt
def add_comment(request, inventario_id):
    if request.method == 'POST':
        inventario = get_object_or_404(Inventario, id_inventario=inventario_id)
        calificacion = request.POST.get('calificacion')
        comentario = request.POST.get('comentario')
        # Assuming you have logged in users, you can get the user from request.user
        # user = request.user
        # Then, you can create a new comment object
        # comment = Comentarios.objects.create(id_producto=inventario.id_producto, calificacion=calificacion, comentario=comentario, fecha=date.today(), usuario=user)
        comment = Comentarios.objects.create(id_producto=inventario.id_producto, calificacion=calificacion, comentario=comentario, fecha=date.today())
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))  # Redirect back to the same page after adding comment
    else:
        return HttpResponseRedirect('/')

@csrf_exempt
def test(request):
    return render(request, "test.html")
