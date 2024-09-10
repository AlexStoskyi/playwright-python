import pytest
from playwright.async_api import async_playwright

from spec.page import HomePage
from spec.page import PopUpPage
from spec.page import ProductPage
from spec.page import ProductDetailPage



@pytest.mark.asyncio
async def test_verify_product_and_detail():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()

        home_page = HomePage.HomePage(page)
        await home_page.goto()

        assert await home_page.is_home_page_visible(), "Home page title mismatch"

        pop_up_page = PopUpPage.PopUpPage(page)
        await pop_up_page.pop_up()
        await pop_up_page.pop_up_confirm_button()

        products_page = ProductPage.ProductPage(page)
        product_detail_page = ProductDetailPage.ProductDetailPage(page)
        await home_page.click_products()

        assert await products_page.is_products_page_visible(), "Products page not visible"

        assert await products_page.is_products_list_visible(), "Products list not visible"

        await products_page.click_first_product_view_button()

        assert await product_detail_page.is_product_detail_visible(), "Product detail page not visible"

        details = await product_detail_page.get_product_details()
        assert details["name"], "Product name is not visible"
        assert details["category"], "Product category is not visible"
        assert details["price"], "Product price is not visible"
        assert details["availability"], "Product availability is not visible"
        assert details["condition"], "Product condition is not visible"
        assert details["brand"], "Product brand is not visible"

        await browser.close()
