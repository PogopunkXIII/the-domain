#!/bin/bash
set -e

mac_address_to_send_wake_on_lan_to=$1

etherwake -i wlan0 $mac_address_to_send_wake_on_lan_to
