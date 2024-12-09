from django import forms
from django.shortcuts import redirect, render
from plant.models import *

# class PostForm(forms.ModelForm):
#     class Meta:
#         model = Post
#         fields = ('name', 'brigade', 'boss')

class EmployeeRegistr(forms.Form):
    name = forms.CharField(max_length=50, label= 'ФИО:')
    position = forms.CharField(max_length=50, label= 'Должность:')
    boss = forms.BooleanField(label='Руководитель:', required=False)
    brigade = forms.CharField(max_length=50, label= 'Бригада:')


class EmployeeForm(forms.Form):
    # class EmployeeForm(forms.ModelForm):
    name = forms.CharField(max_length=50, label= 'ФИО:')
    position = forms.CharField(max_length=50, label= 'Должность:')
    boss = forms.BooleanField(label='Руководитель:', required=False)
    brigade = forms.ChoiceField(label='Бригада:', choices=[(b.id, b.name) for b in Brigade.objects.all()])
    # brigade = forms.ChoiceField(label='Бригада:', choices=[])
    #
    # def __init__(self, *args, **kwargs):
    #     super(EmployeeForm, self).__init__(*args, **kwargs)
    #     self.fields['brigade'].choices = [(b.id, b.name) for b in Brigade.objects.all()]
    # brigade = forms.CharField(max_length=50, label= 'Бригада:')
    # class Meta:
    #     model = Employee
    #     fields = ('name', 'position', 'boss', 'brigade')

class Employee1:
    def __init__(self, name, position):
        """
        Инициализация объекта Employee.

        Args:
            name (str): Имя сотрудника.
            age (int): Возраст сотрудника.
            position (str): Должность сотрудника.
            salary (float): Зарплата сотрудника.
        """
        self.name = name
        # self.age = age
        self.position = position
        # self.salary = salary

    def __str__(self):
        """
        Возвращает строковое представление объекта Employee.
        """
        return f"Имя: {self.name}, Должность: {self.position}"
        # return f"Имя: {self.name}, Возраст: {self.age}, Должность: {self.position}, Зарплата: {self.salary}"