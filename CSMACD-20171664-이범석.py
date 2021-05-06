import time
import random

def persistence():
    tmp = random.randint(0, 1)

    if tmp == 1:
        print("Persistence is not busy. Send data immediately.")
        time.sleep(1)
        return True
    else:
        sec = random.randint(1, 4)
        print("persistence is busy. Send after %d time." %sec)
        time.sleep(sec)
        return persistence()

def transmission():
    print("Transferring data.")
    time.sleep(1)
    send = random.randint(0, 1)
    collision = random.randint(0, 1)

    if send == 1 and collision == 0:
        print("Collision did not occur.")
        return True
    elif send == 0:
        return transmission()
    elif collision == 1:
        print("Collision has occurred.")
        return False

success = 0
fail = 0
k = 3
Tfr = 1

for i in range(0, 15):
    result1 = persistence()
    
    if result1 == True:
        result2 = transmission()
        if result2 == True:
            print("Transfer successful.\n")
            success += 1
            k = 0
            continue
        else:
            print("Transfer failed.")
            print("Send jamming signal.")

            fail += 1
            k += 1
            R = random.randint(0, 2 ** k)

            print("R is %d\n" %R)
            wait = R * Tfr
            time.sleep(wait)
            continue

print("success: %d" %success)
print("fail: %d" %fail)