#!/bin/bash
set -euo pipefail
#pwrstat -status | grep -oP "Load\.* \K([0-9]+)(?= Watt)"

UPS_ADDRESS=nutdev1@localhost

MAX_LOAD_WATTS=815
#CURRENT_LOAD=$(upsc amd-desktop@192.168.10.57 | grep -oP "ups.load: \K(.*)$")
CURRENT_LOAD=$(upsc $UPS_ADDRESS | grep -oP "ups.load: \K(.*)$")

CURRENT_WATTS=$(($MAX_LOAD_WATTS * $CURRENT_LOAD / 100))
echo "${CURRENT_WATTS}"
