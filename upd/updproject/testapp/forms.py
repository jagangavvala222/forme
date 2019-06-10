from django import forms

from testapp.models import  PythonDocument


class DocumentForm(forms.ModelForm):
    class Meta:
        model = PythonDocument
        fields = ('description', 'document', )
