from commands.command import Command
from settings import initial_welcome
import os
import platform


class Clear(Command):
    name = "Clear"
    signature = "clear"
    desc = "Clears the users screen and reprints intro message"
    config = {}

    def __init__(self, cmd):
        super().__init__(cmd)
    
    def _clear(self, command):
        os.system(command)

    def cmd_run(self, *args):
        systems = { "Linux" : 'clear', "Darwin" : 'clear', "Windows" : 'cls' }
        self._clear(systems[platform.system()])
        self.cmd.log(initial_welcome)

