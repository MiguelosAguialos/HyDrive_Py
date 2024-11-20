from logger import logger

class MainException(Exception):
    def __init__(self, msg):
        self.msg = msg