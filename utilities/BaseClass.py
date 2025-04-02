import inspect

import pytest
from _pytest import logging
import logging


@pytest.mark.usefixtures("setup")
class BaseClass:

    def getLogger(self):
        log = inspect.stack()[1][3]
        logger = logging.getLogger(log)
        handler = logging.FileHandler('log_file.log')
        formating = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")
        handler.setFormatter(formating)
        logger.addHandler(handler)
        logger.setLevel(logging.DEBUG)

        return logger

