# It is for Creating the Logs for the Testcases....


import logging


class LogGen:
    @staticmethod
    def loggen():
        logging.basicConfig(filename=".//Logs//Automation.log",
                            format="%(asctime)s;%(levelname)s;%(message)s",
                            datefmt= "%Y-%m-%d %H:%M:%S:%P")
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger

