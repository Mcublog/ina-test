#!/usr/bin/env python

import time

from ina219 import INA219
from ina219 import DeviceRangeError

SHUNT_OHMS = 0.1


def read():
    ina = INA219(SHUNT_OHMS, busnum=1, address=0x40)
    ina.configure(voltage_range=ina.RANGE_32V, gain=ina.GAIN_4_160MV, bus_adc=ina.ADC_64SAMP, shunt_adc=ina.ADC_64SAMP)

    while True:
        try:
            shunt_mv = ina.shunt_voltage()
            # print("Bus Voltage: %.3f V" % ina.voltage())        
            print("Bus Current: %.3f mA" % ina.current())
            # print("Power: %.3f mW" % ina.power())
            print("Shunt voltage: %.3f mV" % shunt_mv)
            print('-' * 15)
        except DeviceRangeError as e:
            # Current out of device range with specified shunt resistor
            print(e)
        time.sleep(0.1)

if __name__ == "__main__":
    read()
