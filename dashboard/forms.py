from django import forms    # Importar los formularios
from .models import *    # Importar nuestros modelos

import datetime
from django.forms.extras.widgets import SelectDateWidget
from django.forms import ModelForm, Form

date_field = forms.DateField(widget=SelectDateWidget)

# Formulario para editar un post
class DateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = DateField(widget = AdminDateWidget)

"""
# Formulario para editar un comentario
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('author', 'text',)
"""
