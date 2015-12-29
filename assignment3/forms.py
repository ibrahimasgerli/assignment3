__author__ = 'ibrahimasgerli'
from django import forms
class Teacher(forms.Form):
    first_name=forms.CharField(max_length=30)
    last_name=forms.CharField(max_length=30)
    office_details=forms.CharField(max_length=60)
    phone=forms.CharField(max_length=20)
    email=forms.EmailField()

class Student(forms.Form):
    first_name=forms.CharField(max_length=30)
    last_name=forms.CharField(max_length=30)
    email=forms.EmailField()

class Course(forms.Form):
    name=forms.CharField(max_length=30)
    code=forms.CharField(max_length=60)
    classroom=forms.CharField(max_length=30)
    times=forms.TimeField()
