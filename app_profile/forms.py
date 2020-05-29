from django.forms import ModelForm
from .models import *

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class MyinfoForm(ModelForm):
    class Meta:
        model = Myinfo
        fields = '__all__'


class LanguageForm(ModelForm):
    class Meta:
        model = Language
        fields = '__all__'


class InterestForm(ModelForm):
    class Meta:
        model = Interest
        fields = '__all__'


class EducationForm(ModelForm):
    class Meta:
        model = Education
        fields = '__all__'


class ExperienceForm(ModelForm):
    class Meta:
        model = Experience
        fields = '__all__'

