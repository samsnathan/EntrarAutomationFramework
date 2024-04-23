import logging


class LogGen:
    @staticmethod
    def loggen():
        logging.basicConfig(filename="automation.log",
                            format='%(asctime)s :%(levelname)s : %(name)s :%(message)s', datefmt='%m %d %Y %I %M %S %p')
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger
