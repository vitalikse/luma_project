from pages.shopping_cart_page import ShoppingCartPage
from data.data_urls import SHOPPING_CART_PAGE, MAIN_PAGE_URL


class TestShoppingCart:

    def test_tc_07_01_01_verify_title_shopping_cart_is_displayed_correctly(self, driver):
        """Check Shopping Cart title is displayed correctly"""
        page = ShoppingCartPage(driver, SHOPPING_CART_PAGE)
        page.open()
        title = page.check_shopping_cart_title()
        assert title == "Shopping Cart", "The title of Shopping Cart is not displayed correctly"

    def test_tc_07_01_03_verify_here_link_is_actual(self, driver):
        """Check that the “here” link is displayed and clickable."""
        page = ShoppingCartPage(driver, SHOPPING_CART_PAGE)
        page.open()
        here_link = page.check_here_link_is_clickable()
        assert here_link is not None, 'The link "here" is not actual'

    def test_tc_07_01_04_verify_here_link_leads_to_the_main_page(self, driver):
        """Verify that the link "here" redirects to the main page."""
        page = ShoppingCartPage(driver, SHOPPING_CART_PAGE)
        page.open()
        actual_link = page.here_link_actual_url()
        assert actual_link == MAIN_PAGE_URL


