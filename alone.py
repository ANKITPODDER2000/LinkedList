import datetime 
import time
def alone():
    now = datetime.datetime.now()
    a = datetime.datetime(now.year, now.month, now.day,
                          now.hour, now.minute, now.second)
    b = datetime.datetime(2021, 1, 1, 23, 56, 10) 
    c = a-b
    sec     = int(c.total_seconds() % 60)
    s = " seconds "
    if sec==1:
        s = " second "
    minutes = c.total_seconds() // 60
    hours   = minutes // 60
    minutes = int(minutes % 60)
    m = " minutes "
    if minutes==1:
        m = " minutes "
    days    = int(hours   // 24)
    d = " days "
    if days==1:
        d = "day"
    hours   = int(hours   % 24 )
    h = " hours "
    if hours==0:
        h = " hour "
    print("Alone : "+str(days)+d+str(hours)+h+str(minutes)+m+str(sec)+s)
def main():
    while True:
        alone()
        time.sleep(1)
if __name__ == "__main__":
    main()
