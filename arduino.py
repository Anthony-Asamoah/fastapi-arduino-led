import logging
import pyfirmata

import time

from config import Defaults


class Interface:
    logging.info('Arduino Startup')

    board = pyfirmata.Arduino(Defaults.arduino_port)
    _ = pyfirmata.util.Iterator(board)
    _.start()
    pins = {
        "green": board.get_pin('d:9:o'),
        "amber": board.get_pin('d:8:o'),
    }

    @staticmethod
    def on(pin):
        return pin.write(1)

    @staticmethod
    def off(pin):
        return pin.write(0)

    @staticmethod
    def show(color: str, wait: int = Defaults.timeout):
        pin = Interface.pins.get(color.lower())
        logging.debug(f'Got pin: {pin} from {color}')

        Interface.on(pin)
        logging.debug(f'{pin} activated')
        time.sleep(wait)
        Interface.off(pin)
        logging.debug(f'{pin} deactivated')

    logging.info('Arduino Initialized. Ready')
