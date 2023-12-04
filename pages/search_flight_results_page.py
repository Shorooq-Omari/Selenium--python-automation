import logging
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from base.base_driver import BaseDriver
from utilities.utils import Util


class SearchFlightResults(BaseDriver):
    log = Util.custom_logger(logLevel=logging.WARNING)
    def __init__(self, driver):
        super().__init__( driver)
        self.driver = driver
       # self.wait = wait

    #Locators
    FILTER_BY_1_STOP_ICON ="//div[@class=' font-lightgrey fs-11 tipsy i-b']//span[@class='dotted-borderbtm'][normalize-space()='1 Stop']"
    FILTER_BY_2_STOP_ICON ="//p[@class='font-lightgrey bold'][normalize-space()='2']"
    FILTER_BY_NON_STOP_ICON ="//p[@class='font-lightgrey bold'][normalize-space()='0']"
    SEARCH_FLIGHT_RESULTS = "//span[contains(text(), 'Non Stop') or contains(text(),'1 Stop') or contains(text(),'2 Stops')]"

    def get_filter_by_non_stop_icon(self):
        return self.driver.find_element(By.XPATH, self.FILTER_BY_NON_STOP_ICON)

    def get_filter_by_1_stop_icon(self):
        return self.driver.find_element(By.XPATH, self.FILTER_BY_1_STOP_ICON)

    def get_filter_by_2_stop_icon(self):
        return self.driver.find_element(By.XPATH, self.FILTER_BY_2_STOP_ICON)

    def get_search_flight_results(self):
        return self.wait_for_presence_of_all_elements(By.XPATH, self.SEARCH_FLIGHT_RESULTS)
    def filter_flights_by_stops(self, by_stop):
        if by_stop == "1 Stop":
            self.get_filter_by_1_stop_icon()
            self.log.warning("Selected flights with 1 stop")
            time.sleep(2)
        elif by_stop == "2 Stops":
            self.get_filter_by_2_stop_icon()
            self.log.warning("Selected flights with 2 stop")
            time.sleep(2)
        elif by_stop == "NON Stop":
            self.get_filter_by_non_stop_icon()
            self.log.warning("Selected flights with NON stop")
            time.sleep(2)
        else:
            self.log.warning("Please provide valid filter option")

        #self.driver.find_element(By.XPATH, "//div[@class=' font-lightgrey fs-11 tipsy i-b']//span[@class='dotted-borderbtm'][normalize-space()='1 Stop']")
        #time.sleep(4)
        #allstops1 = self.wait_for_presence_of_all_elements(By.XPATH,
                                                    #     "//span[contains(text(), 'Non Stop') or contains(text(),'1 Stop') or contains(text(),'2 Stop')")
        #allstops1 = self.wait.until(EC.Presence_of_all_elements_located((By.XPATH, "//span[contain")))
        #print(len(allstops1))


