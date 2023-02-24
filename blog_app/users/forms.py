from django.forms import ModelForm
from django import forms
from .models import Profile, Entries


class EntriesForm(ModelForm):
    class Meta:
        model = Entries
        fields = '__all__'
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['description'].widget.attrs.update({'class':'input', 'placeholder': 'Add text'})