import pytest
from playwright.async_api import async_playwright

from spec.page import HomePage
from faker import Faker
from spec.page import PopUpPage
from spec.page import FooterPage


fake = Faker()



@pytest.mark.asyncio
async def test_subscription_in_home_page():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()

        home_page = HomePage.HomePage(page)
        await home_page.goto()

        assert await home_page.is_home_page_visible(), "Home page title mismatch"

        pop_up_page = PopUpPage.PopUpPage(page)
        await pop_up_page.pop_up()
        await pop_up_page.pop_up_confirm_button()

        footer_page = FooterPage.FooterPage(page)
        await footer_page.scroll_to_footer()

        assert await footer_page.is_subscription_text_visible(), "'SUBSCRIPTION' text is not visible"

        await footer_page.enter_email_and_submit(fake.email())

        assert await footer_page.is_success_message_visible(), "Success message is not visible"

        await browser.close()
