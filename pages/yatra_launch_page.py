import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from base.base_driver import BaseDriver
from pages.search_flight_results_page import SearchFlightResults
from utilities.utils import Util
import logging


class LaunchPage(BaseDriver):
    log = Util.custom_logger()
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        #self.wait = wait

    DEPART_FROM_FIELD = "//input[@id='BE_flight_origin_city']"
    GOING_TO_FIELD = "//input[@id='BE_flight_arrival_city']"
    GOING_TO_RESULT_LIST = "//div[@class='viewport']//div[1]/li"
    SELECT_DATE_FIELD = "//input[@id='BE_flight_origin_date']"
    ALL_DATES = "//div[@id='monthWrapper']//tbody//td[@class!='inActiveTD']"
    SEARCH_BUTTON = "//input[@value='Search Flights']"

    def getDepartFromField(self):
        return self.wait_for_element_to_be_clickable(By.XPATH, self.DEPART_FROM_FIELD)

    def getGoingToFiled(self):
        return self.wait_for_element_to_be_clickable(By.XPATH, self.GOING_TO_FIELD)

    def getGoingToResultField(self):
        return self.wait_for_presence_of_all_elements(By.XPATH, self.GOING_TO_RESULT_LIST)

    def getDepartureDateField(self):
        return self.wait_for_element_to_be_clickable(By.XPATH, self.SELECT_DATE_FIELD)

    def getALLDatesField(self):
        return self.driver.find_elements(By.XPATH, self.ALL_DATES)

    def getSearchButton(self):
        return self.driver.find_element(By.XPATH, self.SEARCH_BUTTON)


    def enterDepartFromLocation(self, departlocation):
        self.getDepartFromField().click()
        self.getDepartFromField().send_keys(departlocation)
        self.getDepartFromField().send_keys(Keys.ENTER)

    def enterGoingToLocation(self, goingtolocation):
        self.getGoingToFiled().click()
        self.log.info("Clicked on going to")
        time.sleep(2)
        self.getGoingToFiled().send_keys(goingtolocation)
        self.log.info("Typed text into going to field successfully")
        time.sleep(2)
        search_result = self.getGoingToResultField()
        for results in search_result:
            if goingtolocation in results.text:
                print(results)
                results.click()
                break

    def enterDepartureDate(self, departuredate):
        self.getDepartureDateField().click()
        time.sleep(2)
        self.wait_for_element_to_be_clickable(By.XPATH, "//div[@id='monthWrapper']//tbody//td[@class!='inActiveTD']")
        all_dates = self.getALLDatesField()
        for date in all_dates:
            if date.get_attribute("data-date") == departuredate:
                date.click()
                print(date)
                break

    def clickSearchFlightButton(self):
        self.getSearchButton().click()
        time.sleep(4)


    def searchFlights(self, departlocation, goingtolocation, departuredate):
        self.enterDepartFromLocation(departlocation)
        time.sleep(2)
        self.enterGoingToLocation(goingtolocation)
        time.sleep(2)
        self.enterDepartureDate(departuredate)
        time.sleep(2)
        self.clickSearchFlightButton()
        time.sleep(2)
        search_flights_result = SearchFlightResults(self.driver)
        time.sleep(2)
        return search_flights_result

    # def departfrom(self, depart_location):
    #    depart_from = self.wait_for_element_to_be_clickable(By.XPATH, "//input[@id='BE_flight_origin_city']")
     #   depart_from.click()
      #  depart_from.send_keys(depart_location)
       # depart_from.send_keys(Keys.ENTER)


    #def goingto(self, goingto_location):
     #   going_to = self.wait_for_element_to_be_clickable(By.XPATH, "//input[@id='BE_flight_arrival_city']")
      #  going_to.click()
       # time.sleep(2)
        #going_to.send_keys(goingto_location)
        #time.sleep(2)
        #search_result = self.wait_for_presence_of_all_elements(By.XPATH, "//div[@class='viewport']//div[1]/li")
            #
        ##self.wait.until(EC.presence_of_all_elements_located((By.XPATH, "//div[@class='viewport']//div[1]/li"))).\

        #for results in search_result:
         #   if "New York (JFK)" in results.text:
          #      print(results)
           #     results.click()
            #    break

#    def selectdate(self, departure_date):
 #       origen = self.wait_for_element_to_be_clickable(By.XPATH, "//input[@id='BE_flight_origin_date']")

  #      origen.click()
   #     time.sleep(2)
    #    self.wait_for_element_to_be_clickable(By.XPATH, "//div[@id='monthWrapper']//tbody//td[@class!='inActiveTD']")
     #   all_dates = self.driver.find_elements(By.XPATH, "//div[@id='monthWrapper']//tbody//td[@class!='inActiveTD']")

      #  for date in all_dates:
       #     if date.get_attribute("data-date") == departure_date:
        #        date.click()
         #       print(date)
          #      break

   # def clicksearch(self):
    #    self.driver.find_element(By.XPATH, "//input[@value='Search Flights']").click()
     #   time.sleep(4)
