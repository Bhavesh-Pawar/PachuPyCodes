import time
hour=int(input("Enter the hours : "))
min=int(input("Enter the minutes : "))
sec=int(input("Enter the seconds : "))
t=60
if(hour>23 or min>59 or sec>59 or hour<0 or min<0 or sec<0):
    print("Enter valid Time ")
    exit(1)
print(hour,":",min,":",sec)
while True:
    sec+=1
    time.sleep(1)
    if sec==60:
        min+=1
        if min==60:
            hour+=1
            if hour==24:
                print("Its Next Day :) ")
                hour=0
                min=0
                sec=0
            min=0
            sec=0
        sec=0
    print(hour,":",min,":",sec)
    t-=1

    