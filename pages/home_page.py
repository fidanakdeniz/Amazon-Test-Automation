from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class HomePage(BasePage):

    REJECT_COOKIE= (By.ID, 'sp-cc-rejectall-link')
    SEARCH_BOX = (By.ID, 'twotabsearchtextbox')
    SEARCH_BUTTON = (By.ID, 'nav-search-submit-button')



    def click_reject_cookie(self):
        self.click_element(*self.REJECT_COOKIE)

    def click_search_box(self):
        self.click_element(*self.SEARCH_BOX)

    def send_search_text(self, search_text):
        self.driver.find_element(*self.SEARCH_BOX).send_keys(search_text)

    def click_search_button(self):
        self.click_element(*self.SEARCH_BUTTON)

    def get_current_url(self):
        return self.driver.current_url


    def is_reject_cookie_visible(self):
        return self.is_element_visible(self.REJECT_COOKIE)

    def is_reject_cookie_clickable(self):
        return self.is_element_clickable(self.REJECT_COOKIE)

    def is_search_box_visible(self):
        return self.is_element_visible(self.SEARCH_BOX)

    def is_search_box_clickable(self):
        return self.is_element_clickable(self.SEARCH_BOX)

    def is_search_button_visible(self):
        return self.is_element_visible(self.SEARCH_BUTTON)

    def is_search_button_clickable(self):
        return self.is_element_clickable(self.SEARCH_BUTTON)









