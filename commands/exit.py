from commands.command import Command

class Exit(Command):
    name = "Exit"
    signature = "exit"
    desc = "Exits the prompt."
    arguments = {}
    config = {}

    def _init_(self, cmd):
        super().__init__(cmd)

    def cmd_run(self, *args):
        self.cmd.running = False
        self.cmd.log("Exiting...")