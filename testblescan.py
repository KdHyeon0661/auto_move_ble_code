import blescan
import sys
from IBeacon import IBeacon
import calc
import bluetooth._bluetooth as bluez
import time

ibeacon = IBeacon()

my_uuid = "aabbccddeeff99"
your_uuid = "00000000000000"
stat = "00"
sock_num = "01"
major = 0
angle = 0
minor = 0
tx = "0xba"
distance = 0.0
connection = time.time()

uuid = my_uuid + sock_num + stat + your_uuid

ibeacon.execute_beacon(uuid, major, minor, tx)

dev_id = 0
try:
    sock = bluez.hci_open_dev(dev_id)
    print("ble thread started")
except:
    print("error accessing bluetooth device...")
    sys.exit(1)

blescan.hci_le_set_scan_parameters(sock)
blescan.hci_enable_le_scan(sock)

while True:
    returnedList = blescan.parse_events(sock, 10)
    for beacon in returnedList:
        val = beacon.split(',')
        tmp_uuid = val[1]
        beacon1 = tmp_uuid[0:14]
        beacon2 = tmp_uuid[14:16]
        beacon3 = tmp_uuid[16:18]
        beacon4 = tmp_uuid[18:32]
        if beacon1 == my_uuid and beacon2 == "04" and beacon3 == stat: # move
            connection = time.time()
            stat = "01"
            your_uuid = beacon4
            uuid = my_uuid + sock_num + stat + your_uuid
            angle = float(val[2]) / 100
            distance = calc.calc_dist(val[4], val[5])
            ibeacon.execute_beacon(uuid, major, minor, tx)

            # prerequisites : know distance, angle
        elif beacon1 == my_uuid and beacon2 == "04" and beacon3 == "02" and beacon4 == your_uuid:
            connection = time.time()
            print("Hello") # hibernate mode
    if stat != "00": # connection lost
        if time.time() - connection > 10:
            your_uuid = "00000000000000"
            stat = "00"
