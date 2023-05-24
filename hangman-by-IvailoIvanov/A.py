# import sys
# import time
# def delay_print(s):
#     for c in s:
#         sys.stdout.write(c)
#         sys.stdout.flush()
#         time.sleep(0.12)
# delay_print("I want this text big")
import sys, time


def delprint(text, delay_time):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(delay_time)


delprint("Ivailo", 0.25)
