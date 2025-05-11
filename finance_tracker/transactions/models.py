from django.db import models


class TransactionType(models.TextChoices):
    EXPENSE = 'EXPENSE', 'Expense'
    INFLOW = 'INFLOW', 'Inflow'


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


def get_default_category():
    category, created = Category.objects.get_or_create(name="Other")
    return category


class Transaction(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    type = models.CharField(max_length=7, choices=TransactionType.choices)
    category = models.ForeignKey(Category, on_delete=models.SET_DEFAULT, default=get_default_category)

    def __str__(self):
        return f"{self.date} - {self.category}: {self.amount} ({self.get_type_display()})"
