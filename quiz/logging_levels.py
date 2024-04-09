class LoggingLevel:
    INFO = 1
    WARNING = 2
    ERROR = 3
    CRITICAL = 4

    @staticmethod
    def from_int(level: int) -> "LoggingLevel":
        if level == 1:
            return LoggingLevel.INFO
        elif level == 2:
            return LoggingLevel.WARNING
        elif level == 3:
            return LoggingLevel.ERROR
        elif level == 4:
            return LoggingLevel.CRITICAL
        else:
            raise ValueError("Invalid logging level")