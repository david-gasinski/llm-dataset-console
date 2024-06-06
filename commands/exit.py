from commands.command import Command

class Exit(Command):
    name = "Exit"
    signature = "exit"
    arguments = []
    desc = "Exits the prompt."
    config = {}

    def _init_(self, cmd):
        super().__init__(cmd)

    def cmd_run(self, *args):
        self.cmd.running = False
        self.cmd.log("Exiting...")