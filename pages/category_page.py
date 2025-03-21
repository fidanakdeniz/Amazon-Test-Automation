from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CategoryPage(BasePage):

    SECOND_PAGE= (By.CSS_SELECTOR, "a.s-pagination-item.s-pagination-button[aria-label='2 sayfasına git']")
    SELECTED_PRODUCT=(By.XPATH, "(//div[@class='a-section aok-relative s-image-square-aspect'])[3]")
    SEARCHED_PRODUCT = (By.CLASS_NAME, 'a-color-state')
    RESULTS=(By.XPATH, "//h2[contains(text(), 'Sonuçlar')]")


    searched_product_text = '"samsung"'
    sonuclar='Sonuçlar'



    def hover_second_page(self):
        self.hover_element(*self.SECOND_PAGE)

    def click_second_page(self):
        self.click_element(*self.SECOND_PAGE)


    def click_selected_product(self):
        self.click_element(*self.SELECTED_PRODUCT)

    def get_searched_product_text(self):
        return self.get_text(self.SEARCHED_PRODUCT)

    def get_results_text(self):
        return self.get_text(self.RESULTS)



    def is_second_page_visible(self):
        return self.is_element_visible(self.SECOND_PAGE)

    def is_second_page_clickable(self):
        return self.is_element_clickable(self.SECOND_PAGE)

    def is_selected_product_visible(self):
        return self.is_element_visible(self.SELECTED_PRODUCT)

    def is_selected_product_clickable(self):
        return self.is_element_clickable(self.SELECTED_PRODUCT
                                         )
