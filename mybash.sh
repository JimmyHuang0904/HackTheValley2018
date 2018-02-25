#!/bin/bash

# PID is from ps aux | grep bluetoothctl
# Need to run strace -pPID -s9999 -e write=0 -o trace.log

while true; do
    RSID_FULL=$(cat trace.log | grep RSSI | tail -1 | cut -d ' ' -f 6)
    RSID=${RSID_FULL::-4}
    #echo $RSID
    python signalStrength.py $RSID

    #sleep 5
done
