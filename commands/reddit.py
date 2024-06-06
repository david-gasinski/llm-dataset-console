from commands.command import Command

class Reddit(Command):
    name = "Reddit API Interface"
    signature = "reddit"
    config = {}

    def __init__(self, cmd):
        super().__init__(cmd)
