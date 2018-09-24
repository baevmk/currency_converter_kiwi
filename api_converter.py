from flask import Flask, request, make_response, jsonify
from wtforms import Form, StringField, TextAreaField, PasswordField, FloatField, validators
from core_converter import ConvertData
import json

app = Flask(__name__)


@app.route('/currency_converter', methods=['GET'])
def currency_converter():
    amount = request.args.get("amount")
    input_currency = request.args.get("input_currency")
    output_currency = request.args.get("output_currency")

    codes = converter.supported_currencies()
    input_currencies = []
    output_currencies = []

    if not input_currency:
        return make_response(jsonify({
            "error": "Missing required value(s)",
            "description": "Missing input_currency"}), 400)
    if not output_currency:
        output_currency = 'ALL'

    for code_key, symbol_value in codes.items():
        if input_currency == code_key or input_currency == symbol_value:
            input_currencies.append(code_key)
        if output_currency == code_key or output_currency == symbol_value:
            output_currencies.append(code_key)
    # Cheking if more than one currencies with the same simbol
    if len(input_currencies) == 1:
        input_currency = input_currencies[0]
    elif len(input_currencies) > 1:
        return make_response(jsonify({
            "error": "Specify value(s)",
            "description": "More than one currencies have the same symbol: " + str(input_currencies)}), 400)
    if len(output_currencies) == 1:
        output_currency = output_currencies[0]
    elif len(output_currencies) > 1:
        return make_response(jsonify({
            "error": "Specify value(s)",
            "description": "More than one currencies have the same symbol: " + str(output_currencies)}), 400)

    try:
        converter.load_currency(float(amount), input_currency, output_currency)

    except Exception as inst:
        print("Error found: " + str(inst))

    return make_response(jsonify(converter.__dict__), 200)


if __name__ == '__main__':
    converter = ConvertData()
    app.run()
