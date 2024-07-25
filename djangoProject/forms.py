from django import forms
from django.contrib.auth.forms import UserCreationForm
from djangoProject.models import Client

def clean_passport(passport_number):
