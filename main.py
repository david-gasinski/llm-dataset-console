import threading
import json
import requests

# settings
from settings import initial_welcome
from settings import invalid_chars
from logger import Logger
from logger import Loggers

# commands
from commands.reddit import Reddit
from commands.exit import Exit
from commands.clear import Clear
from commands.help import Help


class CommandPrompt():
    def __init__(self):
        self.running = True
        self.commands = {}
        self.exec_queue = []
        self.logger = Logger()
        self._init_commands()

    def _init_commands(self):
        self.commands[Reddit.signature] = Reddit(self)
        self.commands[Exit.signature] = Exit(self)
        self.commands[Clear.signature] = Clear(self)
        self.commands[Help.signature] = Help(self)

    def await_input(self):
        valid_int = False
        while not valid_int:
            res = input(" > ")
            valid_int = True  
            self.logger.get_log(Loggers.FILE).warning("Invalid char!", extra=self.logger.extra_config())        
            # checks for invalid characters, need refactoring
            #for char in invalid_chars:
            #    if char in res:
            #        self.logger.get_log(Loggers.CONSOLE).info("Invalid char {invalid_char}".format(invalid_char=char))
            #        break
        return res.split(" ") 

    def log(self, value: str):
        print(value) # goated

    def main(self):
        self.log(initial_welcome)
        while self.running:
            prompt: str = self.await_input()
            
            if self.commands[prompt[0]] is not None:
                self.log("Command {prompt} not found.".format(prompt=prompt[0])) 
                continue # skip iteration as command doesnt exist
            
            self.commands[prompt[0]].cmd_run(*prompt[1:])
        # save any edited files
        self.log("Bye!")    
        
        

if __name__ == '__main__':
    cmd = CommandPrompt()
    cmd.main()
        
        
            