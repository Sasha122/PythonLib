from config import config
from core.comand import  comands
from core.console import Controller
from core.console import StartProject
from colorama import init, Fore, Back, Style
from core.Errors import Errors
from core.admin import admin

def start_app():
    print( Fore.CYAN + "PythonSnake->")
    print(Fore.LIGHTMAGENTA_EX)
    value = input("")
    print(Fore.RESET)
    if(value == comands.comand_list[0]):
        Controller.User_Name()
        start_app()
    elif(value == comands.comand_list[1]):
        Controller.User_Password()
        start_app()
    elif(value == comands.comand_list[2]):
        Controller.Version()
        start_app()
    elif(value == comands.comand_list[3]):
        Controller.CreateProject()
        start_app()

    elif(value == comands.comand_list[4]):
        valueI = input("Выберете варинат: 1 - одна страница index 2 - две страницы")
        if(valueI == "1"):
            print("OK")
            Controller.start_project_template_1()
            start_app()
        elif(valueI == "2"):
            Controller.start_project_template_2()
            start_app()
        else:
            print("ERROR"
                  "")
            start_app()
    elif(value == comands.comand_list[5]):
        Controller.Commands()
        start_app()
    elif(value == comands.comand_list[6]):
        StartProject.Release()
    elif(value == comands.comand_list[7]):
        Controller.Command.Debug(value)
        start_app()
    elif(value == comands.comand_list[8]):
        admin.start('')
    else:
        print( Fore.RED  + value  +  "  -  " + Errors.PrintErrors['3'])
        print(Fore.RESET)
        start_app()






