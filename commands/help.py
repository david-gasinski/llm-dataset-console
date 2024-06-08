from commands.command import Command


class Help(Command):
    name = "Help"
    signature = "help"
    desc = "Helps with a designated command"
    arguments = {"command_type" : str}
    config = {}

    def __init__(self, cmd):
        super().__init__(cmd)
    
    def cmd_run(self, *args):
        target = args[0]
        if not self.cmd.commands[target]:
            self.log("Command {prompt} doesn't exist.".format(prompt=target)) 
            return
        self.cmd.commands[target].cmd_help()
        
