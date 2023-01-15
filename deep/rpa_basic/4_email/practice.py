import time
print(time.strftime("%d-%b-%Y")) # %a: 요일, %b: 월

import datetime
dt = datetime.datetime.strptime("2020-12-30", "%Y-%m-%d")
print(type(dt))
print(dt.strftime("%d-%b-%Y"))