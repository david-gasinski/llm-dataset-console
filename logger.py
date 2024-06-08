import logging.config
import yaml
import enum
import inspect

class Loggers(enum.Enum):
    CONSOLE = "console"
    INFO = "console-info"
    FILE = "file"

class Logger():
    def __init__(self):
        self._load_config()
        self.loggers = {
            "console" : logging.getLogger('console'), 
            "console-info" : logging.getLogger('console-info'),
            "file" : logging.getLogger('file') 
        }

    def _load_config(self):
        with open('config.yaml', 'rt') as f:
            config = yaml.safe_load(f.read())
        logging.config.dictConfig(config)
        
    def get_log(self, log_type : Loggers):
        return self.loggers[log_type.value]    
    
    def extra_config(self):
        return {
            'file' : inspect.currentframe().f_back.f_code.co_filename,
            'func' : inspect.currentframe().f_back.f_code.co_name,
            'line': inspect.currentframe().f_back.f_code.co_firstlineno
        }