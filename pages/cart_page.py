from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CartPage(BasePage):

    DELETE_PRODUCT_BUTTON=(By.XPATH, "//input[@data-feature-id='item-delete-button']")
    MAIN_LOGO=(By.ID, 'nav-logo-sprites')
    CART_COUNT=(By.ID, 'nav-cart-count')
    PRODUCT_COUNT=(By.XPATH,"//span[@data-a-selector='value']")
    COMPLETE_BUTTON=(By.ID, 'sc-buy-box-ptc-button')
    C_PRODUCT_TITLE = (By.CSS_SELECTOR, "#activeCartViewForm div.sc-list-item-content h4")
    C_PRODUCT_PRICE=(By.CSS_SELECTOR, "#activeCartViewForm div.sc-list-item-content div.sc-item-price-block span"
                                    "[class*='product-price'] > span + span")
    SUCCESS_MESSAGE=(By.CSS_SELECTOR, '#NATC_SMART_WAGON_CONF_MSG_SUCCESS h1')

    cart_count='1'
    deleted_cart_count='0'
    product_count='1'
    cart='cart'
    complete_button='Alışverişi Tamamla'


    def click_delete_product_button(self):
        self.click_element(*self.DELETE_PRODUCT_BUTTON)

    def click_main_logo(self):
        self.click_element(*self.MAIN_LOGO)

    def get_cart_count(self):
        #This function is to get the number(count) in the cart icon
        return self.get_text(self.CART_COUNT)

    def get_product_count(self):
        #This function is to get the number(count) of product in the cart
        return self.get_text(self.PRODUCT_COUNT)

    def get_complete_button_text(self):
        #This function is to get the text in the "complete shopping" button
        return self.get_text(self.COMPLETE_BUTTON)

    def get_cart_product_title(self):
        #This function gets the text name of the product on the cart page.
        return self.get_text(self.C_PRODUCT_TITLE)

    def get_cart_product_price(self):
        #This function gets the text price of the product on the cart page
        #The purpose of replace in this function was that the product price came without a comma on the product page
        # but with a comma on the cart page. I made the test work without any problems by using the replace method.
        return self.get_text(self.C_PRODUCT_PRICE).replace(',', '').replace('\n', '').replace('\r', '')

    def get_added_cart_message(self):
        #This function retrieves the "added to cart" text on the next page after the product is added to the cart.
        return self.get_text(self.SUCCESS_MESSAGE).strip()



    def is_delete_product_button_visible(self):
        return self.is_element_visible(self.DELETE_PRODUCT_BUTTON)

    def is_delete_product_button_clickable(self):
        return self.is_element_clickable(self.DELETE_PRODUCT_BUTTON)

    def is_main_logo_visible(self):
        return self.is_element_visible(self.MAIN_LOGO)

    def is_main_logo_clickable(self):
        return self.is_element_clickable(self.MAIN_LOGO)




