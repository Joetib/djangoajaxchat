

from chat.models import UserProfile
from django.contrib.auth.forms import UserCreationForm
from django import forms

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('picture',)