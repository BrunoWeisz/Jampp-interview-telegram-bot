import logging
class LoggingConfiguration:
    def startLogging(this):
        logging.basicConfig(format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s', 
                            level = logging.INFO)