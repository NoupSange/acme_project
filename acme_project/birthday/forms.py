# birthday/forms.py
from django import forms

from django.core.exceptions import ValidationError

# Импортируем класс модели Birthday.
from .models import Birthday

BEATLES = {'Джон Леннон', 'Пол Маккартни', 'Джордж Харрисон', 'Ринго Старр'}

class BirthdayForm(forms.ModelForm):

    class Meta:
        model = Birthday
        fields = '__all__'

        def clean_first_name(self):
            # Получаем значение имени из словаря очищенных данных.
            first_name = self.cleaned_data['first_name']
            # Разбиваем полученную строку по пробелам 
            # и возвращаем только первое имя.
            return first_name.split()[0]

        def clean(self):
            # Получаем имя и фамилию из очищенных полей формы.
            first_name = self.cleaned_data['first_name']
            last_name = self.cleaned_data['last_name']
            # Проверяем вхождение сочетания имени и фамилии во множество имён.
            if f'{first_name} {last_name}' in BEATLES:
                raise ValidationError(
                    'Мы тоже любим Битлз, но введите, пожалуйста, настоящее имя!'
                )
            