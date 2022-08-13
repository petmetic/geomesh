from django import forms


class ReportForm(forms.Form):
    csv_upload = forms.FileField(label='File upload', required=True)
