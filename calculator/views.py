from django.http import JsonResponse
from django.shortcuts import render


# Create your views here.
from calculator.controllers import ExchangeRateController
from calculator.forms import CalculatorForm


def show_index(request):
    erc = ExchangeRateController()
    pairs = erc.get_all_pairs()
    form = CalculatorForm()

    return render(request, 'index.html', {'form': form, 'data': pairs})


def calculate_amount(request):
    erc = ExchangeRateController()
    from_currency = request.GET.get('from_currency', '')
    to_currency = request.GET.get('to_currency', '')
    amount = float(request.GET.get('amount', ''))
    result_amount = erc.calculate_amount(from_currency, to_currency, amount)
    return JsonResponse({'result_amount': result_amount})
