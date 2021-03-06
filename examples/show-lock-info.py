#!/usr/bin/env python

# Import project path
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.realpath(__file__)), '..'))

# Import pyvera
import pyvera

# Parse Arguments
import argparse
parser = argparse.ArgumentParser(description='show-lock-info')
parser.add_argument('-u', '--url', help="Vera URL, e.g. http://192.168.1.161:3480", required=True)
args = parser.parse_args()

# Start the controller
controller, _ = pyvera.init_controller(args.url)

try:
    # Get a list of all the devices on the vera controller
    all_devices = controller.get_devices()

    # Look over the list and find the lock devices
    for device in all_devices:
        if isinstance(device, pyvera.VeraLock):
            print('{} ({})'.format(type(device).__name__, device.name, device.device_id))
            print('    comm_failure: {}'.format(device.comm_failure))
            print('    room_id: {}'.format(device.room_id))
            print('    is_locked(): {}'.format(device.is_locked()))
            print('    get_pin_failed(): {}'.format(device.get_pin_failed()))
            print('    get_unauth_user(): {}'.format(device.get_unauth_user()))
            print('    get_lock_failed(): {}'.format(device.get_lock_failed()))
            print('    get_last_user(): {}'.format(device.get_last_user()))
            print('    get_pin_codes(): {}'.format(device.get_pin_codes()))

finally:
    # Stop the subscription listening thread so we can quit
    controller.stop()

