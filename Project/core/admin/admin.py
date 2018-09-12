from colorama import init, Fore, Back, Style
from core.admin.core import Handler
from core.admin.settings import settings
def start_admin(self):
    print(settings.config['version'])
    Handler.Handler.start('')