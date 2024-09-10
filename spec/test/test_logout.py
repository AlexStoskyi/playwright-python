import pytest
from playwright.async_api import async_playwright

from spec.page import HomePage
from spec.page import SignupPage
from faker import Faker
from spec.page import PopUpPage
from helper.valid_data import VALID_USER_DATA


fake = Faker()
user_datas = VALID_USER_DATA

@pytest.mark.asyncio
async def test_user_logout():
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
        sing_pu_page = SignupPage.SignupPage(page)
        assert await sing_pu_page.is_login_visible(), "'Login to your account' is not visible"

        await sing_pu_page.logining(user_datas['email'], user_datas['password'])
        await sing_pu_page.click_login_button()

        assert await sing_pu_page.is_logged_in_as_visible(user_datas['name']), "'Logged in as username' is not visible"

        await home_page.click_logout()

        assert await home_page.is_url_contains("/login"), "Not redirected to login page"
        await browser.close()
