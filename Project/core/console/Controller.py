import os
from colorama import init, Fore, Back, Style
from core.Errors import Errors
import codecs
#from core.console import StartProject
init(convert=True)


from colorama import *
from config import config
from core.comand import  comands
def Version():
    print(config.version)
def CreateProject():
    value = input("Введите название")
def Project_Name():
    print("Project-Name=>")
    print(config.settings['title'])
def Pause():
    value = input()
def User_Name():
    print("UESRNAME=>")
    print(config.settings['user_name'])
def User_Password():
    print("USERPASSWORD=>")
    print(config.settings['user_password'])
def Commands():
    print(comands.comand_list)
def start_project_template_1():
    BackGround.SearchTemplate("apps/templates/index.php")
    BackGround.Testing("")



def start_project_template_2():
    BackGround.SearchTemplate("apps/templates/index.php")
    BackGround.SearchTemplate("apps/templates/about.php")
    BackGround.Testing("")



class BackGround:
    def SearchTemplate(path):
        if(os.path.exists(path)):
            print(Fore.GREEN +"OK...Все файлы для разработки гтовы!")
           # text = open("core/templates/index.html")
           # text_1 = text.read()
           # file = open(path, "w")
           # file.write(text_1)
            print("OK...!")
            print(Fore.RESET)
        else:
            print(Fore.RED + Errors.PrintErrors['1'])
            print(Fore.RESET)
    def Testing(self):
        if (config.theme == "dark" or config.theme == "light"):
            print(Fore.GREEN + "OK...Все данные казанны верно")
            print(Fore.RESET)
        else:
            print( Fore.RED +  Errors.PrintErrors['1'])
            print(Fore.RESET)
class Command:
    def Debug(self):
        code = input("Введите код ошибки\n")
        if (code == "1"):
            print( Fore.GREEN + Errors.Errors['1'])
            print(Fore.RESET)
        elif(code == "2"):
            print(Fore.GREEN +Errors.Errors['2'])
            print(Fore.RESET)
        elif(code == "3"):
            print(Fore.GREEN + Errors.Errors['3'])
            print(Fore.RESET)
class admin:
    def header(self):
        BackGround.SearchTemplate('apps/templates/index.html')
        BackGround.SearchTemplate('core/Themes/Dark/header.html')
        text = open("core/Themes/Dark/header.html")
        text_1 = text.read()
        file = codecs.open('apps/templates/index.html', "w" , "utf-8")
        file.write(text_1)
    def footer(self):
        BackGround.SearchTemplate('apps/templates/index.html')
        BackGround.SearchTemplate('core/Themes/Dark/footer.html')
        text = open("core/Themes/Dark/footer.html")
        text_1 = text.read()
        file = open('apps/templates/index.html', "a")
        file.write(text_1)
    def content(self):
        BackGround.SearchTemplate('apps/templates/index.html')
        BackGround.SearchTemplate('core/Themes/Dark/content.html')
        text = open("core/Themes/Dark/content.html")
        text_1 = text.read()
        file = open('apps/templates/index.html', "a")
        file.write(text_1)
    class Add:
        def AddParagraph(self):


            print(Fore.CYAN + "Введите текст абзаца:")
            print(Fore.RESET)
            text = input()
            BackGround.SearchTemplate('core/Themes/Dark/content.html')
            files = codecs.open("core/Themes/Dark/content.html" , "a" ,'utf-8')
            files.write("<p>" + text + "</p>")
        def AddCaption(self):
            pass
