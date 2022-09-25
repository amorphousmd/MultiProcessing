import time
import pymemcache

def run_loop():

    client = pymemcache.Client([('127.0.0.1', 5000)])
    value = input("Press key to continue \n")
    for i in range(0,20000):
        sendvalue = "It Is " + str(i)
        client.set('Value', sendvalue)
        print("sent value  ",sendvalue)
        time.sleep(0.005)


if __name__ == "__main__":
    run_loop()
