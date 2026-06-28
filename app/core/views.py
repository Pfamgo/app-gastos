from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from django.shortcuts import render
from app.transactions.models import Transaction


@login_required
def dashboard(request):
    today = datetime.now()
    month_start = today.replace(day=1)

    transactions = Transaction.objects.filter(user=request.user)
    monthly = transactions.filter(date__gte=month_start, date__lte=today)

    total_income = monthly.filter(type='income').aggregate(Sum('amount'))['amount__sum'] or 0
    total_expense = monthly.filter(type='expense').aggregate(Sum('amount'))['amount__sum'] or 0
    balance = total_income - total_expense

    recent = transactions.order_by('-date', '-created_at')[:5]

    return render(request, 'core/dashboard.html', {
        'total_income': total_income,
        'total_expense': total_expense,
        'balance': balance,
        'recent_transactions': recent,
    })
