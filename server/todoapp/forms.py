from django import forms

from todoapp.models import Item

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = [
            'completed', 'text'
        ]