from config import config
from core.comand import comands
from core.console import  Main_Controller
from colorama import init, Fore, Back, Style
init(convert=True)
def Release():
    i = 0
    while i < 10:
        print(Fore.CYAN + "releasing"  + str(i) + "%")
        i = i + 1
        Fore.RESET()
    if(i == 10):
        Main_Controller.start_app()