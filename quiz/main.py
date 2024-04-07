from logger import log_message
from exceptions import InvalidLogMessage

DEBUG = True

try:
    log_message("")
except InvalidLogMessage as e:
    if DEBUG:
        print(f"დაფიქსირდა გამონაკლისი: {e}")