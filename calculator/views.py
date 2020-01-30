from django.http import JsonResponse
from django.shortcuts import render


# Create your views here.
from calculator.models import ExchangeRate


def show_index(request):
    pairs = ExchangeRate.objects.all()
    return render(request, 'index.html', {'data': pairs})


def calculate_amount(request):
    from_currency = request.GET.get('from_currency', '')
    to_currency = request.GET.get('to_currency', '')
    amount = request.GET.get('amount', '')
    print(f'{from_currency} {to_currency} {amount}')
    data = {'amount': 2}
    return JsonResponse(data)
