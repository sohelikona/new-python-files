from plyer import notification
import time


if __name__ == '__main__':
    while True:
        notification.notify(
            title="*****  TAKE A BREAK  *****",
            message="Why are you working so hard, take a break!😀",
            timeout=5)
        time.sleep(300)  