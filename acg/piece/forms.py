from django import forms
from piece.models import *

class PieceForm(forms.ModelForm):
    default_image = forms.ImageField(widget=forms.FileInput(), required=False)
    class Meta:
        model = Piece

