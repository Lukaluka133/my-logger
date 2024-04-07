from exceptions import InvalidLogMessage

def log_message(message):
    if not message or len(message) == 0:
        raise InvalidLogMessage("log მესიჯი არ უნდა იყოს ცარიელი :)")
    print (f"Logging message: {message}")