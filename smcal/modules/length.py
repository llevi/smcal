from smcal.generic_unit_exchange import exchange

module_name = "length"
units = {
    "m": 1,
    "cm": 0.01,
    "km": 1000,
    "inch": 0.0254
}

def calculate(from_unit, to_unit, value):
    result = exchange(from_unit, to_unit, value)
    return result
