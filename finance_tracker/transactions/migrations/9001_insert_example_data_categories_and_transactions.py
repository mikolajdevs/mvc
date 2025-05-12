from django.db import migrations
from django.conf import settings

from transactions.models import Category, Transaction, TransactionType


def insert_example_data_categories_and_transactions(apps, schema_editor):
    if settings.DEBUG:
        categories = [
            'Salary', 'Freelance', 'Investment', 'Tax', 'Rent',
            'Utilities', 'Groceries', 'Entertainment', 'Healthcare', 'Education'
        ]

        for category_name in categories:
            Category.objects.get_or_create(name=category_name)

        salary_category = Category.objects.get(name='Salary')
        tax_category = Category.objects.get(name='Tax')
        rent_category = Category.objects.get(name='Rent')
        utilities_category = Category.objects.get(name='Utilities')
        groceries_category = Category.objects.get(name='Groceries')
        entertainment_category = Category.objects.get(name='Entertainment')
        healthcare_category = Category.objects.get(name='Healthcare')
        education_category = Category.objects.get(name='Education')
        freelance_category = Category.objects.get(name='Freelance')

        transactions = [
            {'amount': 5000, 'date': '2025-01-01', 'type': TransactionType.INFLOW, 'category': salary_category},
            {'amount': 950, 'date': '2025-01-01', 'type': TransactionType.EXPENSE, 'category': tax_category},
            {'amount': 1500, 'date': '2025-01-05', 'type': TransactionType.EXPENSE, 'category': rent_category},
            {'amount': 1000, 'date': '2025-01-10', 'type': TransactionType.INFLOW, 'category': salary_category},
            {'amount': 200, 'date': '2025-02-03', 'type': TransactionType.EXPENSE, 'category': utilities_category},
            {'amount': 75, 'date': '2025-02-05', 'type': TransactionType.EXPENSE, 'category': groceries_category},
            {'amount': 300, 'date': '2025-03-01', 'type': TransactionType.EXPENSE, 'category': entertainment_category},
            {'amount': 250, 'date': '2025-03-02', 'type': TransactionType.EXPENSE, 'category': healthcare_category},
            {'amount': 100, 'date': '2025-03-05', 'type': TransactionType.EXPENSE, 'category': education_category},
            {'amount': 120, 'date': '2025-03-10', 'type': TransactionType.INFLOW, 'category': freelance_category},
            {'amount': 200, 'date': '2025-04-05', 'type': TransactionType.EXPENSE, 'category': healthcare_category}
        ]

        for transaction_data in transactions:
            Transaction.objects.create(
                amount=transaction_data['amount'],
                date=transaction_data['date'],
                type=transaction_data['type'],
                category=transaction_data['category']
            )


class Migration(migrations.Migration):
    dependencies = [
        ('transactions', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(insert_example_data_categories_and_transactions),
    ]
