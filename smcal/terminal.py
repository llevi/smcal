from cmd import Cmd
from smcal import calc
class TerminalPrompt(Cmd):
    intro = "Python interactive shell calculator with unit exchage support.\n Press ? to get available units\nCommand example:\n smcal$ (10+10)*5 inch to cm"
    prompt = "smcal$ "
    def default(whatisthis, line):
        print(calc.calc(line))
    
    def do_help(whatisthis, line):
        calc.load_modules()
        print("Available units for exchage:")
        for keyword in calc.keywords:
           print("- " + keyword) 
