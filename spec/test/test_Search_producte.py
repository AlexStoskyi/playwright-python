import pytest
from playwright.async_api import async_playwright

from spec.page import HomePage
from spec.page import PopUpPage
from spec.page import ProductPage
from helper.valid_data import VALID_USER_DATA



@pytest.mark.asyncio
async def test_search_by_name():
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

        await home_page.click_products()

        assert await products_page.is_products_list_visible(), "Products page not visible"

        assert await products_page.is_products_list_visible(), "Products list not visible"

        search_query = VALID_USER_DATA['itemName']
        await products_page.enter_search_query(search_query)
        await products_page.click_search_button()

        assert await products_page.is_searched_products_visible(), "'SEARCHED PRODUCTS' not visible"

        assert await products_page.are_searched_products_visible(), "Searched products not visible"
        assert await products_page.search_name_is_the_same(search_query)
        await browser.close()
