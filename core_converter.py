from forex_python.converter import CurrencyRates, CurrencyCodes
import json
import sys


class ConvertData(object):
    def __init__(self):
        self.input = {'amount': float(), 'currency': str()}
        self.output = dict()

    def supported_currencies(self):
        currency_rates = CurrencyRates()
        # get all supported currencies from Forex
        codes = dict(currency_rates.get_rates('USD'))
        symbols = CurrencyCodes()
        codes['USD'] = ''
        # get symbols for supported currencies
        for code in codes.keys():
            codes[code] = symbols.get_symbol(code)
        return codes

    def load_currency(self, input_amount, input_curr, output_curr):
        self.input['amount'] = input_amount
        self.input['currency'] = input_curr
        self.output = dict()
        currency_rates = CurrencyRates()

        if output_curr == 'ALL' or output_curr == 'None':
            self.output = dict(currency_rates.get_rates(input_curr))
            self.output.update(
                (result_key, result_value * input_amount) for result_key, result_value in self.output.items())
        else:
            self.output[output_curr] = currency_rates.get_rate(input_curr, output_curr) * input_amount
