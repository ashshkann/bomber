from django.db import models

# Create your models here.

class sms_bomber(models.Model):
    sms_model = models.CharField(max_length=15)

    class Meta:
        verbose_name = 'smsbomber'
        verbose_name_plural = 'smsbombers'
    def __str__(self):
        return self.sms_model

class email_atack(models.Model):
    email_model = models.CharField(max_length=60)

    class Meta:
        verbose_name = 'email atack'
        verbose_name_plural = 'email atacks'
    def __str__(self):
        return self.email_model

   