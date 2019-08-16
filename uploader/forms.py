from django import forms
from uploader.models import Image

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('image', )
        
