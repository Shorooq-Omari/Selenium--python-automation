import time
import pytest
import softest
from pages.yatra_launch_page import LaunchPage
from utilities.utils import Util
from ddt import ddt, data, file_data, unpack


@pytest.mark.usefixtures("setup")
@ddt
class TestSearchAndVerifyFilter(softest.TestCase):
    log = Util.custom_logger()
    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.lp = LaunchPage(self.driver)
        self.ut = Util()

    @data(("New Delhi", "New York", "23/12/2023", "1 Stop"), ("BOMi", "JFK","25/12/2023", "2 Stops"))
    @unpack
    #@file_data("..\\testdata\\testdata.json")
    #@file_data("..\\testdata\\testyml.yaml")

    def test_search_flights_1_stop(self, goingfrom, goingto, date, stops):
        #lp = LaunchPage(self.driver)
        search_flight_result = self.lp.searchFlights(goingfrom, goingto, date)
        self.lp.page_scroll()
        #sf = SearchFlightResults(self.driver)
        search_flight_result.filter_flights_by_stops(stops)
        time.sleep(4)

        allstops1 = search_flight_result.get_search_flight_results()
        self.log.info(len(allstops1))
        #ut = Util()
        try:
            self.ut.assertListItemText(allstops1, stops)
        except Exception as e:
            print(e)


 #   def test_search_flights_2_stop(self):
  #      search_flight_result = self.lp.searchFlights("New Delhi", "New York","23/12/2023")
   #     self.lp.page_scroll()
    #    search_flight_result.filter_flights_by_stops("2 Stops")
     #   time.sleep(4)
      #  allstops1 = search_flight_result.get_search_flight_results()
       # print(len(allstops1))
        ##ut = Util()
        #self.ut.assertListItemText(allstops1, "2 Stops")

    #lp.enterDepartFromLocation("New Delhi")
        #lp.departfrom("New Delhi")
        #lp.enterGoingToLocation("New York")
        #lp.goingto("New York")
        #lp.enterDepartureDate("23/12/2023")
        #lp.selectdate("23/12/2023")
        #lp.clickSearchFlightButton()
        #lp.clicksearch()






