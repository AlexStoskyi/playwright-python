import asyncio

import pytest
from playwright.async_api import async_playwright

from spec.page import HomePage
from spec.page import PopUpPage
from spec.page.TastCasePage import TestCasesPage

@pytest.mark.asyncio
async def test_open_tast_case_page():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()

        home_page = HomePage.HomePage(page)
        await home_page.goto()

        assert await home_page.is_home_page_visible(), "Home page title mismatch"

        pop_up_page = PopUpPage.PopUpPage(page)
        await pop_up_page.pop_up()
        await pop_up_page.pop_up_confirm_button()

        await home_page.click_test_cases()

        test_cases_page = TestCasesPage(page)
        assert await test_cases_page.title_is_visible()

        await browser.close()
