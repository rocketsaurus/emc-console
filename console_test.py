#!/usr/bin/env python3
'''
Script for testing console ports

Flags:
iterations = integer #
port = local port used for serial connection
tolerance = pass fail criteria
verbose = for full log with server and local time

Requires the pyserial and dateutil 3rd party modules

pip install pyserial
pip install dateutil

Find the port you want to use for testing with
ls /dev/tty*
'''
from datetime import datetime as dt
from datetime import timedelta
from dateutil.parser import parse
import serial, pytz, time, argparse

def connect():
    # Connection configuration
    return serial.Serial(
        # Check in terminal with: ls /dev/tty*
        port=args['port'],
        
        baudrate=115200,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS
    )

def get_server_time(log=False):
    '''Writing date returns servers current time'''
    ser.write(b'date\r')
    server_time = ser.readline() # First readline reads b'date\r'
    server_time = ser.readline() # Second readline returns server time
    server_time = parse(server_time)  # Convert to datetime object
    if log:
        print('Server time: {}'.format(server_time))
    return server_time

def get_local_time(log=False):
    '''Time of PC script is running on'''
    tz = pytz.timezone('US/Pacific')
    local = dt.now(tz)
    if log:
        print('Local time: {}'.format(local))
    return local

def time_delay(verbose=False):
    if verbose:
        return get_local_time(True) - get_server_time(True)
    else:
        return get_local_time() - get_server_time()

def flags():
    ap = argparse.ArgumentParser()
    ap.add_argument('-p', '--port', default='/dev/tty.USA19H142P1.1',
            help='Local serial port. Not sure? Check with "ls /dev/tty*"')
    ap.add_argument('-i', '--iterations', type=int, default=10, help='# of times script will repeat')
    ap.add_argument('-t', '--tolerance', type=int, default=1, help='Pass/fail time delay criteria in seconds')
    ap.add_argument('-v', '--verbose', action='store_true')
    return vars(ap.parse_args())

if __name__ == '__main__':
    # Parse Flags
    args = flags()

    # Establish connection
    ser = connect()

    # Check connection is established
    print('Connection Open? {}'.format(ser.is_open))

    # Initial time delay
    init_local = get_local_time(True)
    init_server = get_server_time(True)
    calibration = init_local - init_server
    tolerance = calibration + timedelta(seconds=args['tolerance'])
    print('Calibrated time delay: {}'.format(calibration))
    print('Tolerance: {}'.format(tolerance))

    # Run test
    for i in range(args['iterations']):
        measured_time = time_delay(args['verbose'])
        if measured_time < tolerance:
            print('Measured time: {} - Pass'.format(measured_time))
        else:
            print('Measured time: {} - Fail'.format(measured_time))
            break

        time.sleep(1)
