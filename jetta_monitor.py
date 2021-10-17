

# import obd_io
from obd.obd import OBD
from obd.commands import commands

import sys
from time import sleep


SERIAL_RECON_ATTEMPTS = 5
SERIAL_TIMEOUT = 1


def query(obd, key):
    return obd.query(commands[key]).value

def get_vin(obd):
    return query(obd, 'VIN').decode()

def get_oil_temp(obd):
    return query(obd, 'OIL_TEMP')

def get_intake_manifold_temp(obd):
    return query(obd, 'INTAKE_TEMP')

def get_intake_manifold_pressure(obd):
    return query(obd, 'INTAKE_PRESSURE')

def get_engine_rpm(obd):
    return query(obd, 'RPM')

def get_maf_air_flow_rate(obd):
    return query(obd, 'MAF')

def get_engine_load(obd):
    return query(obd, 'ENGINE_LOAD')

def get_commanded_throttle_actuator(obd):
    return query(obd, 'THROTTLE_ACTUATOR')


def main(serial_path: str):
    # conn = obd_io.OBDConnection(serial_path, SERIAL_BAUDRATE, SERIAL_TIMEOUT,
    #                             SERIAL_RECON_ATTEMPTS, SERIAL_FAST_MODE)
    obd = OBD(portstr=serial_path)

    print('connection status:', obd.interface.status())

    print('VIN:', get_vin(obd))


    while True:
        print()
        print('intake manifold temperature:', get_intake_manifold_temp(obd))
        print('intake manifold pressure:', get_intake_manifold_pressure(obd))
        print('engine rpm:', get_engine_rpm(obd))
        print('MAF:', get_maf_air_flow_rate(obd))
        print('engine load:', get_engine_load(obd))
        print('throttle:', get_commanded_throttle_actuator(obd))
        sleep(0.25)

    obd.close()


if __name__ == '__main__':
    ser = sys.argv[1]
    main(ser)
