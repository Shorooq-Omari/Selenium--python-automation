import inspect
import logging
import softest

class Util(softest.TestCase):

    def assertListItemText(self, list, value):
        for stop in list:
            print("The text is: " + stop.text)
            self.soft_assert(self.assertEqual, stop.text, value)
            if stop.text == value:
                print("assert pass")
            else:
                print("test failed")
        self.assert_all()

    def custom_logger(logLevel=logging.DEBUG):
        #set class/method name from where its called
        logger_name = inspect.stack()[1][3]

        #create logger
        logger = logging.getLogger(logger_name)
        logger.setLevel(logLevel)

        #create console handler or file handler and set the log level
        fh = logging.FileHandler("automation.log")

        #create formatter - how you want your logs to be formatted
        formatter = logging.Formatter('%(asctime)s - %(levelname)s : %(message)s', datefmt='%m/%d/%y %I:%M:%S %p')

        #add formatter to consol or file handler
        fh.setFormatter(formatter)

        #add console handler to logger
        logger.addHandler(fh)
        return logger
