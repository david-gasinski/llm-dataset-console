import dotenv

dotenv.load_dotenv()

initial_welcome = """
v 0.1.0
    Welcome to my custom scripting command prompt!
    Use this to interface with custom python scripts, pass in files as arguments,
    interface with apis. 
    Built with performance in mind, every command runs on an isolated thread so you 
    can execute many commands with custom scripts!

    Commands are case sensitive.
    Run 'help' to view a list of commands!

By David Gasinski
"""

invalid_chars =  '/!"£$%^&*(){}[]'
