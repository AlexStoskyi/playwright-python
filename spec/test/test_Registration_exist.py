import pytest
from playwright.async_api import async_playwright

from spec.page import HomePage
from spec.page import SignupPage
from faker import Faker
from spec.page import PopUpPage
from helper.valid_data import VALID_USER_DATA


fake = Faker()
user_data = VALID_USER_DATA

@pytest.mark.asyncio
async def test_user_registration_exist_email():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()

        home_page = HomePage.HomePage(page)
        await home_page.goto()

        assert await home_page.is_home_page_visible(), "Home page title mismatch"

        pop_up_page = PopUpPage.PopUpPage(page)
        await pop_up_page.pop_up()
        await pop_up_page.pop_up_confirm_button()


        await home_page.click_signup_login()
        signup_page = SignupPage.SignupPage(page)

        assert await signup_page.is_signup_form_visible(), "'New User Signup!' is not visible"


        await signup_page.enter_name_and_email(fake.name(), user_data["email"])
        await signup_page.click_signup_button()

        await signup_page.error_singup_message_visible()

        await browser.close()
