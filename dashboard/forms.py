from django import forms    # Importar los formularios
from .models import *    # Importar nuestros modelos
from django.contrib.admin.widgets import AdminDateWidget

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
