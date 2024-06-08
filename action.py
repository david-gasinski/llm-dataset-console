import collections

class Action():
    def __init__(self, cmd, command):
        self.cmd = cmd
        self.command = command

    def args_type_check(self):
        return
    
    def execute(self):
        try:
            self.command.cmd_run()
        except:
            return
        