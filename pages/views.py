from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView


import os
from django.conf import settings
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.contrib.staticfiles import finders

import random
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.conf import settings
from django.shortcuts import render, redirect
from .models import Pqrs

from django.shortcuts import render, redirect
from django.db import connection
from django.db.utils import OperationalError
from django.urls import reverse


class HomePageView(TemplateView):
    template_name = 'inicio/inicio.html'
    
class NosotrosView(TemplateView):
    template_name = 'inicio/nosotros.html'

    def generar_numero_radicado(self):
        while True:
            numero = str(random.randint(1000000, 9999999))
            if not Pqrs.objects.filter(numero_radicado=numero).exists():
                return numero

    def post(self, request, *args, **kwargs):
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        tipo_pqrs = request.POST.get('tipo_pqrs')
        imagen = request.POST.get('imagen')

        numero_radicado_generado = self.generar_numero_radicado()

        pqrs_obj = Pqrs(
            nombre=name,
            email=email,
            mensaje=message,
            tipo_pqrs=tipo_pqrs,
            numero_radicado=numero_radicado_generado,
            imagen=imagen
        )
        pqrs_obj.save()

        subject = "Confirmación de Recepción de PQRS"

        html_message = render_to_string('email_template.html', {
            'name': name,
            'message': message,
            'tipo_pqrs': tipo_pqrs,
            'numero_radicado_generado': numero_radicado_generado,
        })

        email = EmailMessage(
            subject,
            html_message,
            settings.EMAIL_HOST_USER,
            [email]
        )
        email.content_subtype = "html"

        try:
            email.send()
        except Exception as e:
            return render(request, self.template_name, {'error': 'Error al enviar el correo: {}'.format(str(e))})

        return redirect('nosotros')  

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Aquí puedes agregar datos adicionales al contexto si es necesario
        return context
    
def buscar_pqrs(request):
    mostrar_resultado = False  # Establece mostrar_resultado en False inicialmente
    if request.method == "POST":
        numero_radicado = request.POST.get('numero_radicado')
        try:
            with connection.cursor() as cursor:
                cursor.execute("SELECT mensaje, nombre FROM pqrs WHERE numero_radicado = %s", [numero_radicado])
                pqrs = cursor.fetchone()
                if pqrs:
                    mostrar_resultado = True  # Si se encontró un mensaje, establece mostrar_resultado en True
                    return render(request, 'nosotros.html', {'pqrs': pqrs, 'mostrar_resultado': mostrar_resultado})
                else:
                    return render(request, 'nosotros.html', {'error': 'No se encontró ningún mensaje con el número de radicado proporcionado.', 'mostrar_resultado': mostrar_resultado})
        except OperationalError as e:
            # Manejo de errores al ejecutar la consulta SQL
            return render(request, 'nosotros.html', {'error': 'Error al ejecutar la consulta SQL.', 'mostrar_resultado': mostrar_resultado})
    else:
        # Manejar el caso cuando la solicitud es un método GET
        return render(request, 'nosotros.html', {'mostrar_resultado': mostrar_resultado})  # Pasar mostrar_resultado como False al cargar la página inicialmente

    
def success(request):
    return render(request, "success.html")

def cancel(request):
    return render(request, "cancel.html")

def products(request):
    return render(request, "products.html")

class SaleInvoicePdfView(View):
    def get(self, request, *args, **kwargs):
        try:
            template = get_template('test.html')
            context = {'title': 'Pdf'}
            html = template.render(context)
            response = HttpResponse(content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="report.pdf"'
            pisa_status = pisa.CreatePDF(
                html, dest=response)
            return response
        except:
            pass
        return HttpResponseRedirect(reverse_lazy('erp:comprobantes'))
    