from config import config
from core.comand import  comands
from core.console import Controller
from core.console import StartProject
def start_app():
    print("EnterCommands")
    value = input("")
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
    else:
        print("Error")
        start_app()






