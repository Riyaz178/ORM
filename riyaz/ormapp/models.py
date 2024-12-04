from django.db import models
from django.contrib import admin
class Bank_loan(models.Model):
    Customer_Name=models.CharField(max_length=100)
    Customer_Age=models.IntegerField()
    Loan_Amount=models.IntegerField()
    Loan_Type=models.CharField(max_length=100)
    Loan_Duration=models.DateField()

class Bank_loanAdmin(admin.ModelAdmin):
    list_display=('Customer_Name','Customer_Age','Loan_Amount','Loan_Type','Loan_Duration')