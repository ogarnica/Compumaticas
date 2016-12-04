from datetime import datetime
import time

try:
    while True:
        now = datetime.now()
        dd = str(now.day)
        mm = str(now.month)
        yyyy = str(now.year)
        hour = str(now.hour)
        mi = str(now.minute)
        sec = str(now.second)
        print(dd,'/',mm,'/',yyyy,'  ',hour,':',mi,':',sec)
        time.sleep(1)
except KeyboardInterrupt:
    exit()
