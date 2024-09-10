import pytest
from playwright.async_api import async_playwright

from spec.page import HomePage
from spec.page import SignupPage
from faker import Faker
from spec.page import PopUpPage

fake = Faker()


@pytest.mark.asyncio
async def test_user_registration():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
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

        name = fake.first_name()
        email = fake.email()
        password = fake.password()
        await signup_page.enter_name_and_email(name, email)
        await signup_page.click_signup_button()


        assert await signup_page.is_account_info_visible(), "'ENTER ACCOUNT INFORMATION' is not visible"
        await signup_page.fill_account_details(name, password)
        await signup_page.check_newsletter_and_offers()
        await signup_page.fill_personal_info()
        await signup_page.click_create_account_button()

        assert await signup_page.is_account_created_visible(), "'Account Created!' is not visible"
        await signup_page.click_continue_button()

        assert await signup_page.is_logged_in_as_visible(name), "'Logged in as username' is not visible"

        await signup_page.click_delete_account_button()
        assert await signup_page.is_account_deleted_visible(), "'Account Deleted!' is not visible"
        await signup_page.click_continue_button()

        await browser.close()
