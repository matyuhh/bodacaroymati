from django import forms
from bodapp.models import Invitado

class InvitadoForm(forms.ModelForm):
    class Meta():
        model = Invitado
        fields = ['nombre','apellido','email','si_viene','extra_invitado','mensaje']
