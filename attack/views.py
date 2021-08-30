from django import forms
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .forms import smsbomber_form, emailatack_form
from .bombers.smsbomber import ther
from .bombers.email_attack import amaliyat


def home_attack(request):
    context = {}
    return render(request, 'home_attack.html', context)

# Create your views here.
@login_required(login_url="/login")
def sms_bomber(request):
    form_smsbomber = smsbomber_form(request.POST or None)
    if request.method == 'POST':
        if form_smsbomber.is_valid():
            sms_data_number = form_smsbomber.cleaned_data.get("sms_form")
            number_attack = form_smsbomber.cleaned_data.get("number_attack")
            counter = 0
            if int(number_attack) < 50 :
                counter = int(number_attack)
            if int(number_attack) > 50 :
                counter = 50
            if int(number_attack) > 100 :
                counter = 100
            print(counter)
            for i in range(counter):
                ther(sms_data_number)
            # form_smsbomber = smsbomber_form(None)
            return redirect("/done-attack")
    context = {
        'form_emailatack':form_smsbomber,
    }
    return render(request, "sms_bomber.html", context)

@login_required(login_url="/login")
def email_attack(request):
    form_emailatack = emailatack_form(request.POST or None)
    if request.method == 'POST':
        if form_emailatack.is_valid():
            bomb_email = form_emailatack.cleaned_data.get("email_form")
            message = form_emailatack.cleaned_data.get("message_form")
            number_attack = form_emailatack.cleaned_data.get("number_attack")
            counter = 0
            if int(number_attack) < 50 :
                counter = int(number_attack)
            if int(number_attack) > 50 :
                counter = 50
            if int(number_attack) > 100 :
                counter = 100
            amaliyat(bomb_email, message, counter)
            return redirect("/done-attack")
    context = {
        'form_emailatack':form_emailatack,
    }
    return render(request, "email_attack.html", context)

