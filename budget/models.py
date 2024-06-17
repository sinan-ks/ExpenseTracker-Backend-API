from django.db import models

from django.contrib.auth.models import User

# Create your models here.

class Expense(models.Model):

    title = models.CharField(max_length=200)

    amount = models.PositiveIntegerField()

    expense_categories = (

        ("HomeRent","Home Rent"),
        ("Bills","Bills"),
        ("Transportation","Transportation"),
        ("EMI","EMI"),
        ("Food","Food"),
        ("Education","Education"),
        ("Fuel","Fuel"),
        ("Shopping","Shopping"),
        ("Savings","Savings"),
        ("Entertainment","Entertainment"),
        ("Miscellaneous","Miscellaneous")

    )

    category = models.CharField(max_length=200, choices=expense_categories, default="Miscellaneous")

    created_date = models.DateTimeField(auto_now_add=True)

    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    priority_categories = (

        ("need","need"),
        ("want","want")

    )

    priority = models.CharField(max_length=200, choices=priority_categories, default="need")

    def __str__(self):

        return self.title
    

class Income(models.Model):

    title = models.CharField(max_length=200)

    amount = models.PositiveIntegerField()

    income_categories = (

        ("Salary","Salary"),
        ("Interest","Interest"),
        ("Rental","Rental"),
        ("Business","Business"),
        ("Investment","Investment"),
        ("Pension","Pension")

    )

    category = models.CharField(max_length=200, choices=income_categories, default="Salary")

    created_date = models.DateTimeField(auto_now_add=True)

    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):

        return self.title
