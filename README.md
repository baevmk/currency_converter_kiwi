# Currency Converter task - [Kiwi.com](https://www.kiwi.com/us/) 

## Introduction 

Currency converter is a simple Python 3.7.0 based converter that allows to convert currencies using CLI application and web API. It uses Forex-Python third-party library to get actual rates.

## Requirements

Currency converter is based on Python 3.7.0, Flask 1.0.2 and Forex-python library. 
To install Flask and Forex-python library use Python Package Manager (PIP) command in cli:
```
pip install flask forex-python
```

## Usage
###API request
```rest
http://127.0.0.1:5000/currency_converter?amount=<float>&input_currency=<3 letter currency code or symbol>&output_currency=<3 letter currency code or symbol>
```

###CLI request
```bash
python currency_converter.py --amount <float> --input_currency <3 letter currency code or symbol> --output_currency <3 letter currency code or symbol>
```
Parameters
- `-a, --amount` - amount which we want to convert - float. Required value
- `-i, --input_currency` - input currency - 3 letters name or currency symbol. Required value
- `-o, --output_currency` - requested/output currency - 3 letters name or currency symbol. If output_currency param is missing, convert to all known currencies

CLI currency_converter.py and web API applications return json with following structure:

```json
{
    "input": { 
        "amount": <float>,
        "currency": <3 letter currency code>
    }
    "output": {
        <3 letter currency code>: <float>
    }
}
```

### Example CLI application
```
$ python currency_converter.py --amount 100.0 --input_currency £ --output_currency USD
{
    "input": {
        "amount": 100.0,
        "currency": "GBP"
    },
    "output": {
        "USD": 131.53
    }
}

```
In case that more than one currencies have the same simbols, CLI application will return objects for all cases
```json5
$ python currency_converter.py --amount 100.0 --input_currency $ --output_currency US$
{
    "input": {
        "amount": 100.0,
        "currency": "AUD"
    },
    "output": {
        "USD": 72.78999999999999
    }
}
{
    "input": {
        "amount": 100.0,
        "currency": "CAD"
    },
    "output": {
        "USD": 77.38000000000001
    }
}
{
    "input": {
        "amount": 100.0,
        "currency": "MXN"
    },
    "output": {
        "USD": 5.29
    }
}

```


### Example web API application
Basic usage
```json
http://127.0.0.1:5000/currency_converter?amount=0.9&input_currency=USD&output_currency=£
{
    "input": {
        "amount": 0.9,
        "currency": "USD"
    },
    "output": {
        "GBP": 0.68427
    }
}
```

In case that more than one currencies have the same simbols, web API app will return error
```json
http://127.0.0.1:5000/currency_converter?amount=0.9&input_currency=$&output_currency=£
{
    "description": "More than one currencies have the same symbol: ['AUD', 'CAD', 'MXN']",
    "error": "Specify value(s)"
}
```
