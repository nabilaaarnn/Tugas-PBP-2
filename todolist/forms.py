from django import forms
from todolist.models import todolistItem

class taskform(forms.ModelForm):
    class Meta:
        model = todolistItem
        fields = {"title", "description"}