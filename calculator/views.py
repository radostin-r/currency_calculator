from django.shortcuts import render


# Create your views here.
from calculator.controllers import ExchangeRateController
from calculator.forms import CalculatorForm


def show_index(request):
    erc = ExchangeRateController()
    pairs = erc.get_all_pairs()

    if request.method == 'POST':
        form = CalculatorForm(request.POST)

        if form.is_valid():
            from_currency = form.cleaned_data['from_currency']
            to_currency = form.cleaned_data['to_currency']
            amount = form.cleaned_data['amount']
            result_amount = erc.calculate_amount(from_currency, to_currency, amount)
            return render(request, 'index.html', {'form': form, 'data': pairs, 'result_amount': result_amount})
    else:
        form = CalculatorForm()

    return render(request, 'index.html', {'form': form, 'data': pairs})

