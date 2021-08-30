from django import forms
from .models import sms_bomber, email_atack

class smsbomber_form(forms.Form):
    sms_form = forms.CharField(
        widget=forms.TextInput(attrs={'class':'form-control'}),
        label=False
    )
    number_attack = forms.CharField(
        widget=forms.NumberInput(attrs={'class':'form-control'}),
        label=False
    )

    
    def clean_sms_form(self):
        sms_form = self.cleaned_data.get("sms_form")
        if "+989" not in sms_form:
            raise forms.ValidationError("bayad az +98 dar shomare khod estefade konin")

        is_exists_user_by_username = sms_bomber.objects.filter(sms_model=sms_form).exists()
        if not is_exists_user_by_username:
            data_sms = sms_bomber(sms_model=sms_form)
            data_sms.save()
        
        return sms_form

class emailatack_form(forms.Form):
    email_form = forms.CharField(
        widget=forms.EmailInput(attrs={'class':'form-control'}),
        label=False
    )
    message_form = forms.CharField(
        widget=forms.TextInput(attrs={'class':'form-control'}),
        label=False
    )
    number_attack = forms.CharField(
        widget=forms.NumberInput(attrs={'class':'form-control'}),
        label=False
    )
    
    def clean_email_form(self):
        email_form = self.cleaned_data.get("email_form")
        if "@" not in email_form:
            raise forms.ValidationError("lotfan email motabar vared konin")

        is_exists_user_by_email = email_atack.objects.filter(email_model=email_form).exists()
        if not is_exists_user_by_email:
            print("nabood!!!")
            data_sms = email_atack(email_model=email_form)
            data_sms.save()

        return email_form
