import os
import pytest
from selenium import webdriver

driver = None
@pytest.fixture(autouse=True)
def setup(request, browser, url):
    global driver
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    elif browser == "edge":
        driver = webdriver.Edge()
    driver.get(url)
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()

def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--url")

@pytest.fixture(scope="class", autouse=True)
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture(scope="class", autouse=True)
def url(request):
    return request.config.getoption("--url")

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    pytest_html = item.config.pluginmanager.getplugin("html")
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, "extra", [])
    if report.when == "call":
        #always add url to report
        extra.append(pytest_html.extras.url("http://www.example.com/"))
        xfail = hasattr(report, "wasxfail")
        if (report.skipped and xfail) or (report.failed and not xfail):
            # only add additional html on failure
            report_directory = os.path.dirname(item.config.option.htmlpath)
            # #file_name = str(int(round(item.time()*1000)))+".png"
            file_name = report.nodeid.replace("::", "_")+".png"
            destinationFile = os.path.join(report_directory, file_name)
            driver.save_screenshot(destinationFile)
            ##if file_name:
            html='<div><img src="%s" alt="screenshot" style="width:200px;height=200px"'\
                'onclick= "windows.open(this.src)" align="right"/></div>'%file_name
            extra.append(pytest_html.extras.html(html))
    report.extras = extra

    #extra.append(pytest_html.extras.url("http://rcvacademy.com/"))
        #xfail = hasattr(report, "wasxfail")
        #if(report.skipped and xfail) or (report.failed and not xfail):
         #   #only add additional html on failure
          #  report_directory = os.path.dirname(item.config.option.htmlpath)
           # #file_name = str(int(round(item.time()*1000)))+".png"
            #file_name = report.failed.replace("::", "_")+".png"
            #destinationFile = os.path.join(report_directory, file_name)
            ##driver.save_screenshots(destinationFile)
            #driver.save_screenshot(".\\test1.png")
            ##if file_name:
            #html='<div><img src="%s" alt="screenshot" style="width:200px;height=200px"'\
             #   'onclick= "windows.open(this.src)" align="right"/></div>'%file_name
            #extra.append(pytest_html.extras.html(html))
        #report.extras = extra

def pytest_html_report_title(report):
    report.title = "Automation Report"

#    driver = webdriver.Chrome()
 #   driver.get("https://www.yatra.com")
  #  driver.maximize_window()
   # #wait = WebDriverWait(driver, 10)
    #request.cls.driver = driver
    ##request.cls.wait = wait
    #yield
    #driver.close()