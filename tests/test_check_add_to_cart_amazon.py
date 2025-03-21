import time

from pages.cart_page import CartPage
from pages.category_page import CategoryPage
from pages.home_page import HomePage
from pages.product_page import ProductPage
from tests.base_test import BaseTest


class TestCheckAddToCartAmazon(BaseTest):
    def test_check_amazon_add_to_cart(self):

        """ 1. Go to https://www.amazon.com.tr/
            2. Verify that you are on the home page
            3. Type 'samsung' in the search field at the top of the screen and perform search.
            4. Verify that there are results for Samsung on the page that appears.
            5. Click on the 2nd page from the search results and verify that the 2nd page is
            currently displayed on the page that opens.
            6. Go to the 3rd Product page from the top
            7. Verify that you are on the product page
            8. Add the product to the cart
            9. Verify that the product has been added to the cart
            10. Go to the cart page
            11. Verify that you are on the cart page and that the correct product has been added to
            the cart
            12. Delete the product from the cart and verify that it has been deleted
            13. Return to the home page and verify that it is on the home page """


        home_page = HomePage(self.driver)
        self.assertTrue(home_page.is_reject_cookie_visible(),"Reject cookie is not visible")
        self.assertTrue(home_page.is_reject_cookie_clickable(),"Reject cookie is not clickable")
        home_page.click_reject_cookie()
        self.assertEqual(self.base_url, home_page.get_current_url(), "You are not in the Amazon home page")
        self.assertTrue(home_page.is_search_box_visible(),"Search box is not visible")
        self.assertTrue(home_page.is_search_box_clickable(),"Search box is not clickable")
        home_page.click_search_box()
        home_page.send_search_text("samsung")
        self.assertTrue(home_page.is_search_button_visible(),"Search button is not visible")
        self.assertTrue(home_page.is_search_button_clickable(),"Search button is not clickable")
        home_page.click_search_button()

        category_page = CategoryPage(self.driver)
        self.assertEqual(category_page.searched_product_text, category_page.get_searched_product_text(),"Samsung "
                                                                                  "products was not found on the page")
        self.assertEqual(category_page.sonuclar, category_page.get_results_text(), "Samsung products was not found"
                                                                                   " on the page")
        category_page.hover_second_page()
        self.assertTrue(category_page.is_second_page_visible(),"Second page button is not visible")
        self.assertTrue(category_page.is_second_page_clickable(),"Second page button is not clickable")
        category_page.click_second_page()
        self.assertIn("page=2", category_page.get_current_url(), "You are not in the second page.")
        self.assertTrue(category_page.is_selected_product_visible(),"Selected product is not visible")
        self.assertTrue(category_page.is_selected_product_clickable(),"Selected product is not clickable")
        category_page.click_selected_product()

        product_page = ProductPage(self.driver)
        self.assertEqual(product_page.buy_now_button,product_page.get_buy_now_button_text(), "You are not in the"
                                                                                             " product page")
        self.assertTrue(product_page.is_add_to_cart_button_visible(),"Add to cart button is not visible")
        self.assertTrue(product_page.is_add_to_cart_button_clickable(),"Add to cart button is not clickable")

        product_title_product_page=product_page.get_product_title()
        product_price_product_page=product_page.get_product_price()

        product_page.click_add_to_cart_button()

        cart_page = CartPage(self.driver)
        time.sleep(5)
        self.assertEqual("Sepete eklendi", cart_page.get_added_cart_message(), "Product was not added to cart")
        self.assertEqual(cart_page.cart_count,cart_page.get_cart_count(),"Product was not added to cart")
        self.assertTrue(product_page.is_go_to_cart_button_visible(),"Go to cart button is not visible")
        self.assertTrue(product_page.is_go_to_cart_button_clickable(),"Go to cart button is not clickable")
        product_page.click_go_to_cart_button()
        self.assertEqual(cart_page.complete_button, cart_page.get_complete_button_text(),"You are not in the cart page")
        self.assertIn(cart_page.cart, self.driver.current_url, "You are not in the cart page")

        product_title_cart_page=cart_page.get_cart_product_title()
        product_price_cart_page=cart_page.get_cart_product_price()

        print(f"\nProduct title on product page:", product_title_product_page)
        print(f"Product price on product page:", product_price_product_page)
        print(f"Product title on cart page:", product_title_cart_page)
        print(f"Product price on cart page:", product_price_cart_page, "\n")

        self.assertEqual(product_title_product_page,product_title_cart_page, "The title of the product added to"
                                                        " the cart does not match the expected product title")
        self.assertEqual(product_price_product_page,product_price_cart_page,"The price of the product added to"
                                                        " the cart does not match the expected product price")
        self.assertEqual(cart_page.product_count,cart_page.get_product_count(),"The product quantity does not "
                                                                     "match expected product quantity value")
        self.assertTrue(cart_page.is_delete_product_button_visible(),"Delete product button is not visible")
        self.assertTrue(cart_page.is_delete_product_button_clickable(),"Delete product button is not clickable")
        cart_page.click_delete_product_button()
        self.assertEqual(cart_page.deleted_cart_count,cart_page.get_cart_count(),"Product was not removed from the"
                                                                                                        " cart")
        self.assertTrue(cart_page.is_main_logo_visible(),"Main logo is not visible")
        self.assertTrue(cart_page.is_main_logo_clickable(),"Main logo is not clickable")
        cart_page.click_main_logo()
        self.assertEqual(self.base_url, cart_page.get_current_url().split("ref")[0], "You are not in the Amazon"
                                                                                                     " home page")
        """Here, to prevent additional parameters from affecting the validation process, I applied split("ref")[0] and
         took the part of the URL before the "ref" parameter and compared it with the base URL. This way, I reliably
          checked whether the user was actually on the homepage, regardless of the redirect."""




























