from django import forms

from .models import UserReport


class ReportForm(forms.ModelForm):
    class Meta:
        model = UserReport
        fields = ['input_file']

    input_file = forms.FileField(label='File upload', required=True)
