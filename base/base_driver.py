import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class BaseDriver:
    def __init__(self, driver):
        self.driver = driver

    def page_scroll(self):
        page_length = self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight); var PageLength=document.body.scrollHeight")
        match = False
        while match == False:
            last_count = page_length
            time.sleep(4)
            page_length = self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight); var PageLength=document.body.scrollHeight")
            if last_count == page_length:
                match = True

        time.sleep(4)

    def wait_for_presence_of_all_elements(self, locator_type, locator):
        try:
            wait = WebDriverWait(self.driver, 10)
            list_of_elements = wait.until(EC.presence_of_all_elements_located((locator_type, locator)))
            return list_of_elements
        except Exception as e:
            print(e)

    def wait_for_element_to_be_clickable(self, locator_type, locator):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.element_to_be_clickable((locator_type, locator)))
        return element
