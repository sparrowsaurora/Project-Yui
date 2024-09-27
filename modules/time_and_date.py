import datetime
import pytz
from modules import voice_input, speech_output

def print_wa_time():
    tz = pytz.timezone('Australia/Perth')
    now = datetime.datetime.now(tz)
    print(now.strftime('%Y-%m-%d %H:%M:%S'))

print_wa_time()