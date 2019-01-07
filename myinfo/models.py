from django.db import models

# Create your models here.
class Myinfo(models.Model):
    inx = models.AutoField(primary_key=True)
    id = models.CharField(max_length=20, blank=True, null=False)
    name_reg = models.CharField(max_length=50, blank=True, null=True)
    jumin_number = models.CharField(max_length=50, blank=True, null=True)
    sex_reg = models.CharField(max_length=10, blank=True, null=True)
    email_reg = models.CharField(max_length=100, blank=True, null=True)
    marry_reg = models.CharField(max_length=10, blank=True, null=True)
    phone_number = models.CharField(max_length=50, blank=True, null=True)
    amount_reg = models.FloatField(default=0)
    myaccount_reg = models.CharField(max_length=50, blank=True, null=True)
    myaccount_password = models.CharField(max_length=50, blank=True, null=True)

class Trade_info(models.Model):
    inx = models.AutoField(primary_key=True)
    gubun = models.CharField(max_length=10, blank=True, null=True)
    value_reg = models.CharField(max_length=100, blank=True, null=True)
    date_reg = models.DateTimeField(blank=True, null=True)
    desc_reg = models.CharField(max_length=50, blank=True, null=True)

class SR_info(models.Model):
    inx = models.AutoField(primary_key=True)
    date_reg = models.DateTimeField(blank=True, null=False)
    send_id = models.CharField(max_length=20, blank=True, null=False)
    receive_id = models.CharField(max_length=20, blank=True, null=False)
    name_reg = models.CharField(max_length=50, blank=True, null=True)
    jumin_number = models.CharField(max_length=50, blank=True, null=True)
    sex_reg = models.CharField(max_length=10, blank=True, null=True)
    email_reg = models.CharField(max_length=100, blank=True, null=True)
    marry_reg = models.CharField(max_length=10, blank=True, null=True)
    phone_number = models.CharField(max_length=50, blank=True, null=True)
    amount_reg = models.FloatField(default=0)
    send_money = models.FloatField(default=0)
    value_reg = models.CharField(max_length=100, blank=True, null=True)
    status_reg = models.BooleanField(blank=True, null=True)
    gubun_reg = models.CharField(max_length=100, blank=True, null=True)

    def publish(self):
        self.save()

    def __str__(self):
        return self.inx