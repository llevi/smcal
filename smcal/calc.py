# Todo: Importing modules and update keywords can be automated
from smcal.generic_unit_exchange import getKeywords
module_names = ["length", "currency"]
modules = {}
keywords = {}

def load_modules():    
    for i in module_names:
        modules[i] = __import__("smcal.modules." + i, fromlist=[i])
        keywords.update(getKeywords(modules[i]))

load_modules()
def calc(line):
    result = 0
    unit_from = 0
    unit_to = 0
    subresult = ""
    for i in line.split():
        
        for j in keywords:
            if j == i:
                if unit_from == 0:
                     unit_from = i
                else:
                     unit_to = i
        if unit_from == 0:
            subresult += str(i)
    if unit_from == 0:
        result = eval(subresult)
    else:
        if modules[keywords[unit_from]["module_name"]] != modules[keywords[unit_to]["module_name"]]:
            print("Error! Cannot convert from " + keywords[unit_from]["module_name"] + " to " + keywords[unit_to]["module_name"])
            return 0
        result = modules[keywords[unit_from]["module_name"]].calculate(keywords[unit_from]["exchange_value"], keywords[unit_to]["exchange_value"], eval(subresult))
    return result

