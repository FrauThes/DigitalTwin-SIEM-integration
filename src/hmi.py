"""
FP hmi.py
"""

from minicps.devices import HMI
from utils import HMI_DATA, STATE
from utils import HMI_PROTOCOL, PLC1_ADDR
from utils import HMI_PERIOD_SEC

import time

ACTUATOR1_1 = ('ACTUATOR1-MV', 1)


class FPHMI(HMI):

    def main_loop(self, sleep=0.0):
        """hmi main loop.
                    - monitor PLC1 tag (actuator1)
                """

        print 'DEBUG: FP HMI enters main_loop.'
        print

        while(True):
            # network capabilities
            self.send(ACTUATOR1_1, 1, PLC1_ADDR)  # open actuator

        time.sleep(HMI_PERIOD_SEC)
        print 'DEBUG FP HMI shutdown'


if __name__ == "__main__":

    hmi = FPHMI(
        name='hmi',
        state=STATE,
        protocol=HMI_PROTOCOL,
        memory=HMI_DATA,
        disk=HMI_DATA)