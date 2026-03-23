from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi, noop
from luma.core.legacy import show_message

# 1. Setup hardware (SPI connection)
serial = spi(port=0, device=0, gpio=noop())
device = max7219(serial, cascaded=1, block_orientation=90)

# 2. Get input and display it
msg = input("Enter your text: ")
delay = float(input("Enter scroll delay (e.g., 0.05): "))

print("Displaying...")
show_message(device, msg, fill="white", scroll_delay=delay)
