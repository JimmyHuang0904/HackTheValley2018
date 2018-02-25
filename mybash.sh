#!/bin/bash

while true; do
    RSID_FULL=$(cat trace.log | grep RSSI | tail -1 | cut -d ' ' -f 8)
    RSID=${RSID_FULL::5}

    echo $RSID

    sleep 10
done
