import time
import os
import pandas

while True:
    if os.path.exists("/home/srana/Documents/temp.csv"):
        data = pandas.read_csv("/home/srana/Documents/temp.csv")
        print(data.mean())
    else:
        print("File does not exist")
    time.sleep(10)