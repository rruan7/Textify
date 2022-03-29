
from django import forms
from .models import Textify
 
 
# creating a form
class TextifyForm(forms.ModelForm):
 
    # create meta class
    class Meta:
        # specify model to be used
        model = Textify
 
        # specify fields to be used
        fields = [
            "image",
        ]