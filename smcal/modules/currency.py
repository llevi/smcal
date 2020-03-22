from smcal.generic_unit_exchange import exchange
import requests
import json
module_name = "currency"

def getCurrencies():
    r = requests.get(url = "https://api.exchangeratesapi.io/latest")
    rates = r.text.lower()
    rates = json.loads(rates)
    rates = rates["rates"]
    for i in rates:
        rates[i] = 1/rates[i]
    rates["eur"] = 1
    return rates

units = getCurrencies();

def calculate(from_unit, to_unit, value):
    result = exchange(from_unit, to_unit, value)
    return result
