from django import forms
from .models import ShortURL

class ShortenerForm(forms.ModelForm):
    original_url = forms.URLField(
        widget=forms.URLInput(attrs={
            'class': 'url-input', 
            'placeholder': 'Paste your long link here...'
        })
    )
    
    class Meta:
        model = ShortURL
        fields = ['original_url']