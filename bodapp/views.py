from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from bodapp.forms import InvitadoForm
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
#  Create your views here.

class IndexView(TemplateView):
    template_name = 'index.html'

class ViajeView(TemplateView):
    template_name = 'viaje.html'

class FotosView(TemplateView):
    template_name = 'fotos.html'

class BodaView(TemplateView):
    template_name = 'boda.html'

class RegalosView(TemplateView):
    template_name = 'regalos.html'

#class RegistroView(FormView):
#    template_name = 'registro.html'
#    form_class = InvitadoForm
#    success_url =  ''

#     def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
#        form.send_email()
#        return super().form_valid(form)

def registro(request):
    if request.method == 'POST':
        form = InvitadoForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('')
    else:
        form = InvitadoForm()
    return render(request, 'registro.html',{'form':form})