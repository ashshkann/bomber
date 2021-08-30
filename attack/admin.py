from django.contrib import admin
from .models import sms_bomber, email_atack
# Register your models here.

admin.site.register(sms_bomber)
admin.site.register(email_atack)
