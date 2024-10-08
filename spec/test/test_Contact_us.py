import asyncio

import pytest
from playwright.async_api import async_playwright

from spec.page import HomePage
from faker import Faker
from spec.page import PopUpPage
from helper.valid_data import VALID_USER_DATA
from helper.message_data import MESSAGE_DATA
from spec.page import ContactUsPage


fake = Faker()
fake_message = fake.sentence()



@pytest.mark.asyncio
async def test_contact_us():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()

        home_page = HomePage.HomePage(page)
        await home_page.goto()

        assert await home_page.is_home_page_visible(), "Home page title mismatch"

        pop_up_page = PopUpPage.PopUpPage(page)
        await pop_up_page.pop_up()
        await pop_up_page.pop_up_confirm_button()


        await home_page.click_contact_us()

        contact_us_page = ContactUsPage.ContactUsPage(page)
        assert await contact_us_page.verify_contact_us_page(), "'GET IN TOUCH' not visible"

        await contact_us_page.fill_contact_form(
            VALID_USER_DATA['name'],
            VALID_USER_DATA['email'],
            VALID_USER_DATA['subject'],
            fake_message
        )

        await contact_us_page.upload_file(VALID_USER_DATA['file'])

        await contact_us_page.click_submit()

        await contact_us_page.confirm_alert()

        assert await contact_us_page.verify_success_message(MESSAGE_DATA['success_message'])
        #Тут проблема з попапом, він зникає до того як підтвердити
        await contact_us_page.click_home_button()

        assert await home_page.is_home_page_visible(), "Home page not visible after clicking 'Home' button"


        await browser.close()
