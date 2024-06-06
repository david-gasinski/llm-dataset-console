class Command():
    name = ""
    signature = ""
    config = {}
    desc = ""

    def __init__(self, cmd):
        self.cmd = cmd

    def cmd_run(self, *args):
        return
    
    def cmd_help(self):
        self.cmd.log("""
            name : {name}
            signature : {sig}
            desc : {desc}
        """.format(name=self.name,sig=self.signature,desc=self.desc))
                 