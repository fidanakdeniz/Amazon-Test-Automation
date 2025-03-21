from selenium.common import WebDriverException
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait



class BasePage(object):
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def find(self, *locator):
        #This function finds a web element.
        return self.driver.find_element(*locator)

    def click_element(self, *locator):
        #This function clicks on the web element it finds.
        self.driver.find_element(*locator).click()

    def hover_element(self, *locator):
        #This function performs the mouseover operation on a web element.
        element = self.find(*locator)
        hover = ActionChains(self.driver).move_to_element(element)
        hover.perform()

    def get_current_url(self):
        #This function gets the URL of the site it is located on.
        return self.driver.current_url

    def wait_element(self, method, message=''):
        #This function waits until the web element becomes clickable.
        return self.wait.until(ec.element_to_be_clickable(method), message)

    def get_text(self, locator):
        #This function retrieves the text inside a web element.
        return self.wait_element(locator).text

    def send_keys(self, *locator, text):
        #This function is used to write text into a specified input field.
        self.driver.find_element(*locator).send_keys(text)

    def is_element_visible(self, locator):
        #This function checks whether the web element is visible or not.
        try:
            self.wait.until(ec.visibility_of_element_located(locator))
            print(f"Element with {locator} is visible")
            return True
        except WebDriverException:
            print(f"Element with {locator} is not visible")
            return False


    def is_element_clickable(self, locator):
        #This function checks whether the web element is clickable or not.
        try:
            self.wait.until(ec.element_to_be_clickable(locator))
            print(f"Element with {locator} is clickable")
            return True
        except WebDriverException:
            print(f"Element with {locator} is not clickable")
            return False















