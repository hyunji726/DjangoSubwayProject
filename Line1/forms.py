# DjangoProject\blogProject\blog\forms.py

from django import forms
from .models import Line1

class PostModelForm(forms.ModelForm):
    class Meta:
        model = Line1
        fields = ['name', 'stations', 'description']  # 입력받을 필드를 정의