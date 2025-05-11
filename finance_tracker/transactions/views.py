from django.db.models import Sum
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect
from django.views import generic

from .forms import TransactionForm
from .models import Transaction


class IndexView(generic.ListView):
    template_name = "transactions/index.html"
    context_object_name = "transactions"

    def get_queryset(self):
        return Transaction.objects.order_by("-date")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        inflows = Transaction.objects.filter(type='INFLOW')
        expenses = Transaction.objects.filter(type='EXPENSE')

        total_inflows = inflows.aggregate(total_inflows=Sum('amount'))['total_inflows'] or 0
        total_expenses = expenses.aggregate(total_expenses=Sum('amount'))['total_expenses'] or 0

        balance = total_inflows - total_expenses
        context['balance'] = balance
        return context


def add(request):
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('transactions:index')
    else:
        form = TransactionForm()
    return render(request, 'transactions/add.html', {'form': form})


def details(request, pk):
    transaction = get_object_or_404(Transaction, pk=pk)
    if request.method == 'POST':
        form = TransactionForm(request.POST, instance=transaction)
        if form.is_valid():
            form.save()
            return redirect('transactions:index')
    else:
        form = TransactionForm(instance=transaction)

    return render(request, 'transactions/edit.html', {'form': form, 'transaction': transaction})


def delete(request, pk):
    transaction = get_object_or_404(Transaction, pk=pk)
    if request.method == 'POST':
        transaction.delete()
        return redirect('transactions:index')
    return HttpResponse(status=405)
