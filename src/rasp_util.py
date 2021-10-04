import os
import time
import datetime

def getCurrentTimeString():
	now_time = datetime.datetime.now()         
    return now_time.strftime("%H:%M:%S")
 
def getCPUTemp():
    temp = os.popen("vcgencmd measure_temp").readline()
    return (temp.replace("temp=", "").replace("'C\n'",""))

if __name__ == '__main__':
    now_temp = getCPUTemp()
    print("Time:", getCurrentTimeString(), "/ Temp:", getCPUTemp())
