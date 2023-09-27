from django import forms
from .models import Subject
from .models import Test


class CSVUploadForm(forms.Form):
    csv_file = forms.FileField(label='Upload question paper ', widget=forms.ClearableFileInput(attrs={'class': 'q-upload'}))


class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ['sub_code', 'sub_name']


class TestForm(forms.ModelForm):
    class Meta:
        model = Test
        fields = ['subject_code', 'subject_name', 'num_questions', 'test_duration', 'start_time']
        widgets = {
            'subject_code': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'type': "text", "id": "subject_code",
                    "name": "subject_code",
                    "required": True
                }),
            'subject_name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'type': "text",
                    "id": "subject_name",
                    "name": "subject_name",
                    "required": True
                }),
            'num_questions': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'type': "number",
                    "id": "num_questions",
                    "name": "num_questions",
                    "required": True
                }),
            'test_duration': forms.DateTimeInput(
                attrs={
                    'class': 'form-control',
                    'type': 'datetime-local',
                    'id': 'test_duration',
                    'name': 'test_duration',
                    'required': True
                }),
            'start_time': forms.DateTimeInput(
                attrs={
                    'class': 'form-control',
                    'type': "datetime-local",
                    "id": "start_time",
                    "name": "start_time",
                    "required": True
                }),
        }
