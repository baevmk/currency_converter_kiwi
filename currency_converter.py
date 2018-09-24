import argparse
import json
from core_converter import ConvertData
import sys


def codes_check(currency_name):
    # Get all currencies/symbols dict
    codes = converted_data.supported_currencies()
    requested_currencies = []
    # Checking which currencies supported/requeted, create list with currencies
    for code_key, symbol_value in codes.items():
        if currency_name == code_key or currency_name == symbol_value:
            requested_currencies.append(code_key)
    if not requested_currencies:
        sys.exit('Currency ' + currency_name + ' not supported. Supported currencies: \n' + str(
            converted_data.supported_currencies()))
    else:
        return requested_currencies


arg_parser = argparse.ArgumentParser()
arg_parser.add_argument('-a', '--amount', help="Amount which you want to convert")
arg_parser.add_argument('-i', '--input_currency', help="Input currency - 3 letters name or currency symbol")
arg_parser.add_argument('-o', '--output_currency',
                        help="Requested/Output currency - 3 letters name or currency symbol. If output_currency param is missing or ALL, convert to all known currencies")

arguments = arg_parser.parse_args()

converted_data = ConvertData()
# Checking input and output
input_currencies = codes_check(str(arguments.input_currency))
if not arguments.output_currency:
    output_currencies = ['ALL']
else:
    output_currencies = codes_check(str(arguments.output_currency))

for input_currency in input_currencies:
    for output_currency in output_currencies:
        try:
            converted_data.load_currency(float(arguments.amount), str(input_currency),
                                         str(output_currency))
            print(json.dumps(converted_data.__dict__, indent=4, sort_keys=True))


        except Exception as inst:
            print("Error found: " + str(inst))
