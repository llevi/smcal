def exchange(from_unit_value, to_unit_value, value):
    referenced_value = from_unit_value * value
    return referenced_value / to_unit_value 

def getKeywords(mod):
    keywords = {}
    for key in mod.units:
        keywords[key] = {"module_name": mod.module_name, "exchange_value":  mod.units[key]}
    return keywords
