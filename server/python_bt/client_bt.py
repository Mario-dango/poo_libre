
"""PyBluez simple example l2capclient.py
Demo L2CAP client for bluetooth module.
$Id: l2capclient.py 524 2007-08-15 04:04:52Z albert $
"""
#94:17:00:DD:74:5F
#941700DD745F
# 98:D3:31:FC:96:5F - HC-06
#Bawy

import sys

import bluetooth
from bluetooth import *

sock = bluetooth.BluetoothSocket(bluetooth.L2CAP)

"""
if len(sys.argv) < 2:
    print("Usage: l2capclient.py <addr>")
    sys.exit(2)
"""

#bt_addr = "94:17:00:DD:74:5F"
bt_addr = "98:D3:31:FC:96:5F"

port = 0x1001

print("Trying to connect to {} on PSM 0x{}...".format(bt_addr, port))

sock.connect((bt_addr, 1))

print("Connected. Type something...")
while True:
    data = input()
    if not data:
        break
    sock.send(b'data')
    data = sock.recv(1024)
    print("Data received:", str(data))

sock.close()
