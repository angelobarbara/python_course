"""User forms."""

# Django
from django import forms
from django.contrib.auth.models import User
from users.models import Profile

class SignupForm(forms.Form):
    username = forms.CharField(min_length=4,max_length=50,required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(min_length=4,max_length=70,widget=forms.PasswordInput(attrs={'class': 'form-control'}),required=True)
    password_confirmation = forms.CharField(min_length=4,max_length=70,widget=forms.PasswordInput(attrs={'class': 'form-control'}),required=True)
    first_name = forms.CharField(min_length=2,max_length=50,required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(min_length=2,max_length=50,required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.CharField(min_length=6,max_length=70,widget=forms.EmailInput(attrs={'class': 'form-control'}),required=True)

    def clean_username(self):
        """Username must be unique"""
        username = self.cleaned_data['username']
        exist_username = User.objects.filter(username=username).exists()
        if exist_username:
            raise forms.ValidationError('Username is already in use')
        return username

    def clean(self):
        """Verify password confirmation match."""
        data = super().clean()
        password = data['password']
        password_confirmation = data['password_confirmation']

        if password != password_confirmation:
            raise forms.ValidationError('Passwords do not match.')

        return data

    def save(self):
        """Create user and profile."""
        data = self.cleaned_data
        data.pop('password_confirmation')

        user = User.objects.create_user(**data)
        profile = Profile(user=user)
        profile.save()


class ProfileForm(forms.Form):
    """Profile form."""

    website = forms.URLField(max_length=200, required=True)
    biography = forms.CharField(max_length=500, required=False)
    phone_number = forms.CharField(max_length=20, required=False)
    picture = forms.ImageField()
