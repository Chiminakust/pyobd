

import obd_io

import serial
import sys


SERIAL_BAUDRATE = 'AUTO'
SERIAL_RECON_ATTEMPTS = 5
SERIAL_TIMEOUT = 1
SERIAL_FAST_MODE = 'FAST'


def main(serial_path: str):
    conn = obd_io.OBDConnection(serial_path, SERIAL_BAUDRATE, SERIAL_TIMEOUT,
                                SERIAL_RECON_ATTEMPTS, SERIAL_FAST_MODE)

    print(conn.connection.status())

    for i in range(10):
        res = conn.get_dtc()
        print(i, res)

    conn.close()


if __name__ == '__main__':
    ser = sys.argv[1]
    main(ser)
