import time

attempts = 0
retries = 5
waitTime = 1

while attempts < retries:
    print(f"Attempt #{attempts+1} , Waiting time : {waitTime}")
    time.sleep(waitTime)
    waitTime *= 2
    attempts += 1
