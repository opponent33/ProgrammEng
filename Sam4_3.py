from datetime import datetime
import time


for i in range(5):
    now = datetime.now()
    curr_time = now.strftime("%H:%M:%S")
    print(f"Current time is {curr_time}")
    time.sleep(1)
    