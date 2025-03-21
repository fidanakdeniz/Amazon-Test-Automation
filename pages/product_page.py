from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class ProductPage(BasePage):

    ADD_TO_CART_BUTTON=(By.ID, 'add-to-cart-button')
    GO_TO_CART_BUTTON = (By.LINK_TEXT, 'Sepete Git')
    BUY_NOW_BUTTON=(By.ID,'submit.buy-now-announce')
    P_PRODUCT_TITLE= (By.CSS_SELECTOR, '#ppd span#productTitle')
    P_PRODUCT_PRICE=(By.CSS_SELECTOR, "#ppd div#corePriceDisplay_desktop_feature_div span[class*='priceToPay']")

    buy_now_button='Şimdi Al'

    def click_add_to_cart_button(self):
        self.click_element(*self.ADD_TO_CART_BUTTON)

    def click_go_to_cart_button(self):
        self.click_element(*self.GO_TO_CART_BUTTON)

    def get_buy_now_button_text(self):
        #This function gets the text of the "buy now" button.
        return self.get_text(self.BUY_NOW_BUTTON)

    def get_product_title(self):
        #This function gets the text name of the product on the product page.
        return self.get_text(self.P_PRODUCT_TITLE).strip()

    def get_product_price(self):
        #This function gets the text price of the product on the product page
        #The purpose of replace in this function was that the product price came without a comma on the product page
        # but with a comma on the cart page. I made the test work without any problems by using the replace method.
        return self.get_text(self.P_PRODUCT_PRICE).replace(',', '').replace('\n', '').replace('\r', '')


    def is_add_to_cart_button_visible(self):
        return self.is_element_visible(self.ADD_TO_CART_BUTTON)

    def is_add_to_cart_button_clickable(self):
        return self.is_element_clickable(self.ADD_TO_CART_BUTTON)

    def is_go_to_cart_button_visible(self):
        return self.is_element_visible(self.GO_TO_CART_BUTTON)

    def is_go_to_cart_button_clickable(self):
        return self.is_element_clickable(self.GO_TO_CART_BUTTON)