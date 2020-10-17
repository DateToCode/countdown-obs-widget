import time

secondTime = 15


while secondTime != 0:
    secondTime -= 1
    f = open("countdown.txt", "w")
    f.write(f"{secondTime//60:02d}:{secondTime%60:02d}")
    f.close()
    time.sleep(1)
