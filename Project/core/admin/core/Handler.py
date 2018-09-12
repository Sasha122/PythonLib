from colorama import init, Fore, Back, Style
from core.admin import admin
from core.comand import comands
from core.console.Controller import  admin
from core.Errors import Errors
class Handler:
    def start(self):
        print(Fore.LIGHTCYAN_EX + "PythonSnake-admin")
        print(Fore.RESET)
        value = input()
        if (value == comands.admin_comands[0]):
            admin.header('')
            Handler.start('')
        elif(value == comands.admin_comands[1]):
            admin.footer('')
            Handler.start('')
        elif(value == comands.admin_comands[2]):
            admin.Add.AddParagraph('')
            Handler.start('')
        elif(value == comands.admin_comands[3]):
            admin.Add.AddCaption('')
            Handler.start()
        elif(value == comands.admin_comands[4]):
            admin.content('')
            Handler.start('')
        elif(value == comands.comand_list[5]):
            print( "admin" + str(comands.admin_comands) + "\n\n\n\n" + "default" + str(comands.comand_list))
            Handler.start('')
        else:

            print(Fore.RED + value + "  -  " + Errors.PrintErrors['3'])
            print(Fore.RESET)
            Handler.start('')