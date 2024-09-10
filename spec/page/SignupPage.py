from playwright.async_api import Page
from faker import Faker

fake = Faker()

class SignupPage:
    def __init__(self, page: Page):
        self.page = page

    async def is_signup_form_visible(self):
        return await self.page.is_visible("//div[@class='signup-form']/h2")

    async def enter_name_and_email(self, name: str, email: str):
        await self.page.fill("//div[@class='signup-form']/form/input[@data-qa='signup-name']", name)
        await self.page.fill("//div[@class='signup-form']/form/input[@data-qa='signup-email']", email)

    async def click_signup_button(self):
        await self.page.click("//div[@class='signup-form']/form/button")

    async def is_account_info_visible(self):
        return await self.page.is_visible("//div/h2[@class='title text-center']")

    async def fill_account_details(self, name: str, password: str):
        await self.page.click("(//div/div[@class='radio-inline'])[1]")
        await self.page.fill("input[name='password']", password)
        await self.page.select_option("select[name='days']", "10")
        await self.page.select_option("select[name='months']", "5")
        await self.page.select_option("select[name='years']", "1990")

    async def check_newsletter_and_offers(self):
        await self.page.check("input[name='newsletter']")
        await self.page.check("input[name='optin']")

    async def fill_personal_info(self):
        await self.page.fill("input[name='first_name']", fake.first_name())
        await self.page.fill("input[name='last_name']", fake.last_name())
        await self.page.fill("input[name='company']", fake.company())
        await self.page.fill("input[name='address1']", fake.address())
        await self.page.fill("input[name='address2']", fake.secondary_address())
        await self.page.select_option("select[name='country']", "United States")
        await self.page.fill("input[name='state']", fake.state())
        await self.page.fill("input[name='city']", fake.city())
        await self.page.fill("input[name='zipcode']", fake.zipcode())
        await self.page.fill("input[name='mobile_number']", fake.phone_number())

    async def click_create_account_button(self):
        await self.page.click("button[data-qa='create-account']")

    async def is_account_created_visible(self):
        return await self.page.is_visible("h2:has-text('Account Created!')")

    async def click_continue_button(self):
        await self.page.click("a[data-qa='continue-button']")

    async def is_logged_in_as_visible(self, name: str):
        return await self.page.is_visible(f'//li[10]//a[1]')

    async def click_delete_account_button(self):
        await self.page.click("a[href='/delete_account']")

    async def is_account_deleted_visible(self):
        return await self.page.is_visible("h2:has-text('Account Deleted!')")

    async def is_login_visible(self):
        return await self.page.is_visible("//h2[text()='Login to your account']")

    async def logining(self, email: str, password: str):
        await self.page.fill("input[name='email']", email)
        await self.page.fill("input[name='password']", password)

    async def click_login_button(self):
        await self.page.click("button[type='submit']")

    async def error_login_message_visible(self):
        return await self.page.is_visible("//form[@action='/login']/p")

    async def error_singup_message_visible(self):
        return await self.page.is_visible("//form[@action='/signup']/p")
