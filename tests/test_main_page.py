"""This section contains home page tests"""
import json
import time

import allure
import pytest

from pages.main_page import MainPage, PromoBlock
from data.data_urls import MAIN_PAGE_URL, ImageUrls
from data.main_data import product_card_button


class TestMainPage:
    class TestHotSellerSection:

        def test_verify_the_card_is_interactive_on_hover(self, driver):
            """This test checks that the card is interactive"""
            page = MainPage(driver, MAIN_PAGE_URL)
            page.open()
            shadow_before, shadow_after = page.check_for_shadow_appearance_when_hovering_over_the_card()
            assert shadow_before != shadow_after, \
                "Card is not interactive"

        def test_verify_the_card_has_title(self, driver):
            """This test checks that the card has title"""
            page = MainPage(driver, MAIN_PAGE_URL)
            page.open()
            title_text = page.check_product_card_title()
            assert len(title_text) > 0, "Card has no title"

        def test_check_for_duplicate_titles_after_clicking_on_the_card(self, driver):
            """This test checks for the same titles after clicking on the product card and going to the product page"""
            page = MainPage(driver, MAIN_PAGE_URL)
            page.open()
            text_before, text_after = page.check_the_correct_page_title_after_click_on_the_card()
            assert text_before == text_after, \
                "Headers are not equal or redirect to the wrong page of the site"

        def test_check_card_price(self, driver):
            """This test checks that the card has a price and a price in USD"""
            page = MainPage(driver, MAIN_PAGE_URL)
            page.open()
            text = page.check_card_price()
            assert len(text) > 0 and "$" in text, "The price is not present and does not contain the $ sign"

        def test_check_card_rating(self, driver):
            """This test checks that if a product has a review, then the product card has a rating"""
            page = MainPage(driver, MAIN_PAGE_URL)
            page.open()

        def test_tc_06_01_08_check_btn_add_to_cart_is_visible(self, driver):
            """This test checks that button Add to Cart is visible on the product card when hover by product"""
            page = MainPage(driver, MAIN_PAGE_URL)
            page.open()
            assert page.btn_is_visible(), 'Button Add to Cart is not visible on the product card'

        @allure.title("TC 06.01.09 - check the color change to add to cart button")
        def test_tc_06_01_09_check_the_color_change_to_add_to_cart_button(self, driver):
            """This test check the color change when hovering over the Add to Cart button"""
            page = MainPage(driver, MAIN_PAGE_URL)
            page.open()
            background_before, background_after = \
                page.check_the_color_change_to_add_to_cart_button()
            assert background_before != background_after, "Product card button did not change color on hover"

        @pytest.mark.parametrize("item", product_card_button)
        def test_tc_06_01_10_check_the_cursor_change_to_cart_button(self, driver, item):
            """This test check the cursor change when hovering over the cart buttons"""
            page = MainPage(driver, MAIN_PAGE_URL)
            page.open()
            cursor_before, cursor_after = page.check_the_cursor_change_to_cart_buttons(item)
            assert cursor_before != cursor_after, "Mouse cursor has not changed"

    class TestPromoBlock:

        def test_tc_13_01_01_check_promo_block_display(self, driver):
            """This test checks if Promo Block under header is displayed on the main page"""
            page = PromoBlock(driver, MAIN_PAGE_URL)
            page.open()
            promo_block = page.check_promo_block_display()
            assert promo_block is True, "The element is not visible"

        def test_tc_13_01_16_check_image_in_section_2_block_1(self, driver):
            """This test checks if the info block image in section 2 block 1 'home-pants' is correct
            in the Promo Block under header on the main page"""
            page = PromoBlock(driver, MAIN_PAGE_URL)
            page.open()
            info_block_image = page.check_block_image_in_section2_block1()
            assert info_block_image == ImageUrls.SECTION_2_BLOCK_1_IMAGE_URL, "The image is not correct"

        def test_tc_13_01_17_check_info_block_in_section2_block1(self, driver):
            """This test checks if info block in section 2 block 1 'home-pants' is displayed
            in the Promo Block under header on the main page"""
            page = PromoBlock(driver, MAIN_PAGE_URL)
            page.open()
            info_block = page.check_info_block_display_in_section2_block1()
            assert info_block is True, "The element is not visible"

        def test_tc_13_01_18_check_info_block_title_in_section2_block1(self, driver):
            """This test checks if the info block title in section 2 block 1 'home-pants' is correct
            in the Promo Block under header on the main page"""
            page = PromoBlock(driver, MAIN_PAGE_URL)
            page.open()
            info_block_title = page.check_info_block_title_in_section2_block1()
            assert info_block_title == "20% OFF", "The title is not correct"

        def test_tc_13_01_19_check_info_block_text_in_section2_block1(self, driver):
            """This test checks if the info block text in section 2 block 1 'home-pants' is correct
            in the Promo Block under header on the main page"""
            page = PromoBlock(driver, MAIN_PAGE_URL)
            page.open()
            info_block_text = page.check_info_block_text_in_section2_block1()
            assert info_block_text == "Luma pants when you shop today*", "The text is not correct"

        def test_tc_13_01_20_check_info_block_sing_in_section2_block1(self, driver):
            """This test checks if the sign in info block in section 2 block 1 'home-pants' is correct
            in the Promo Block under header on the main page"""
            page = PromoBlock(driver, MAIN_PAGE_URL)
            page.open()
            info_block_sign = page.check_info_block_sign_in_section2_block1()
            assert info_block_sign == "Shop Pants", "The text is not correct"
