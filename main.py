import threading
import json
import requests

# settings
from settings import initial_welcome
from settings import invalid_chars

# commands
from commands.reddit import Reddit
from commands.exit import Exit
from commands.clear import Clear
from commands.help import Help


class CommandPrompt():
    def __init__(self):
        self.running = True
        self.commands = []
        self.command_signatures = []
        self._init_commands()
        self._command_signatures()

    def _init_commands(self):
        self.commands.append(Reddit(self))
        self.commands.append(Exit(self))
        self.commands.append(Clear(self))
        self.commands.append(Help(self))

    def _command_signatures(self):
        for command in self.commands:
            self.command_signatures.append(command.signature) 

    def await_input(self):
        valid_int = False
        while not valid_int:
            res = input("\n > ")
            for char in invalid_chars:
                if char in res:
                    self.log("Invalid char {invalid_char}".format(invalid_char=char))
                    self.log("disallowed: {disallowed}".format(disallowed=invalid_chars))
            valid_int = True
        return res.split(" ") 

    def log(self, value):
        print(value) # goated

    def main(self):
        self.log(initial_welcome)
        while self.running:
            prompt = self.await_input()     
            if not prompt[0] in self.command_signatures:
                self.log("Command {prompt} not found.".format(prompt=prompt[0])) 
                pass # skip iteration as command doesnt exist
            for command in self.commands:
                if prompt[0].__eq__(command.signature):
                    command.cmd_run(prompt[1:])
        # save any edited files
        self.log("Bye!")    
        
        

if __name__ == '__main__':
    cmd = CommandPrompt()
    cmd.main()
        
        
            