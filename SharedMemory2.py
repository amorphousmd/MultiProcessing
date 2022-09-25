import pymemcache

if __name__ == "__main__":
    # print("Keys ", keys)
    value = input("Press key to continue \n")
    do_loop = True
    i = 1
    client = pymemcache.Client([('127.0.0.1', 5000)])
    # for key in keys:
    while do_loop:
        ret_value = client.get('Value')
        if ret_value != None:
            print("Value returned is ", ret_value)
