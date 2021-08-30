from django import forms
from django.contrib.auth.models import User


class login_form(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        label=False
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        label=False
    )


class register_form(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        label=False
    )
    email = forms.CharField(
        widget=forms.EmailInput(attrs={'class': 'form-control'}),
        label=False
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        label=False
    )
    re_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        label=False
    )

    def clean_email(self):
        email = self.cleaned_data.get('email')
        is_exists_user_by_email = User.objects.filter(email=email).exists()
        if is_exists_user_by_email:
            raise forms.ValidationError('this email in the database ')

        if len(email) > 20:
            raise forms.ValidationError('must you  half 20 caracter')
        
        if "@gmail.com" not in email:
            raise forms.ValidationError("please input valid email")

        return email
    
    def clean_username(self):
        username = self.cleaned_data.get("username")
        is_exists_user_by_username = User.objects.filter(username=username).exists()
        if is_exists_user_by_username:
            raise forms.ValidationError("this username i the database")
        
        if len(username) > 20:
            raise forms.ValidationError('must you  lower 20 caracter')

        return username

    def clean_re_password(self):
        password = self.cleaned_data.get("password")
        re_password = self.cleaned_data.get("re_password")
        if password != re_password:
            raise forms.ValidationError("the password dosnt match")

        return password