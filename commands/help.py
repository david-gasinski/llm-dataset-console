from commands.command import Command


class Help(Command):
    name = "Help"
    signature = "help"
    arguments = {"command_type" : str}
    desc = "Helps with a designated command"
    config = {}

    def __init__(self, cmd):
        super().__init__(cmd)
    
    def cmd_run(self, *args):
        print(args)
        if args == None:
            for command in self.cmd.commands:
                command.cmd_help()
        
        target = args[0]
        for command in self.cmd.commands:
            if target == command.signature:
                command.cmd_help()
        
