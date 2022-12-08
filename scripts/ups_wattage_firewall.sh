#!/bin/bash
set -euo pipefail

# From the CP1500AVRLCDa spec sheet
MAX_LOAD_WATTS=815

# SNMP MIB for load percentage
SNMP_MIB="SNMPv2-SMI::mib-2.33.1.4.4.1.5.3"

# Get the load integer only.
CURRENT_LOAD=$(snmpget -Oqv -v2c -c public 192.168.10.1 $SNMP_MIB)

# Convert the percentage into wattage consumed right now.
CURRENT_WATTS=$(($MAX_LOAD_WATTS * $CURRENT_LOAD / 100))

echo "${CURRENT_WATTS}"
