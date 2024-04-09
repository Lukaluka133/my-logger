from exceptions import InvalidLogMessage

def log_message(message):
    if not message or len(message) == 0:
        raise InvalidLogMessage("log მესიჯი არ უნდა იყოს ცარიელი :)")
    print (f"Logging message: {message}")

    import logging
    from .logging_levels import LoggingLevel

    class Logger:
        def __init__(self, name: str, level: LoggingLevel = LoggingLevel.INFO):
            self.logger = logging.getLogger(name)
            self.logger.setLevel(level)

        def info(self, message: str):
            self.logger.info(message)

        def warning(self, message: str):
            self.logger.warning(message)

        def error(self, message: str):
            self.logger.error(message)

        def critical(self, message: str):
            self.logger.critical(message)