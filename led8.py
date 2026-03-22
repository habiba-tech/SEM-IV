// sudo pip3 install luma.led_matrix --break-system-packages
//sudo pip3 install luma.core --break-system-packages


import time 
from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi, noop
from luma.core.legacy import text, show_message

def demo():
    serial = spi(port=0 , device=0, gpio=noop)
    device = max7219(serial, cascade=1, block_orintation=90)
    print("led matrix")
    msg = "led matrix demo"
    print(msg)

    show_message(device, msg, fill="white", scroll_delay=0.05)
    time.sleep(0.5)

    #user input
    msg = input("Enter your name")
    sd = float(input("enter delay of scroll value :"))
    print("Dispalying your message")

    show_message(device, msg, fill="white", scroll_delay=0.05)
    time.sleep(0.5)

    print ("Alternative font")
    show_message(device, msg, fill="white", scroll_delay=0.1)

if __name__ == "__main__":
    try:
        demo()
    except KeyboardInterrupt:
        print("Program stopped by user")
        pass            
