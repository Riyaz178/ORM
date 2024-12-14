# Ex02 Django ORM Web Application
## Date:  4:12:24
## AIM
To develop a Django application to store and retrieve data from a bank loan database using Object Relational Mapping(ORM).

## ENTITY RELATIONSHIP DIAGRAM
![WhatsApp Image 2024-12-14 at 13 20 10_437fc346](https://github.com/user-attachments/assets/29e992ad-03fe-4dac-a325-33c26f842643)



## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create details for 10 books

## PROGRAM
```
admin.py
from django.contrib import admin
from .models import Bank_loan,Bank_loanAdmin
admin.site.register(Bank_loan,Bank_loanAdmin)

models.py
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
```


## OUTPUT
![alt text](<Screenshot 2024-12-04 112708.png>)
![alt text](<Screenshot 2024-12-04 113417.png>)


## RESULT
Thus the program for creating a database using ORM hass been executed successfully
