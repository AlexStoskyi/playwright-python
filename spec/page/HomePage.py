from playwright.async_api import Page

class HomePage:
    def __init__(self, page: Page):
        self.page = page

    async def goto(self):
        await self.page.goto("https://automationexercise.com")

    async def is_home_page_visible(self):
        return await self.page.title() == "Automation Exercise"

    async def click_signup_login(self):
        await self.page.click("//div/ul/li/a[@href='/login']")

    async def click_logout(self):
        await self.page.click("//div/ul/li/a[@href='/logout']")

    async def is_url_contains(self, expected_part: str):
        current_url = self.page.url
        return expected_part in current_url

    async def click_contact_us(self):
        await self.page.click("//div/ul/li/a[@href='/contact_us']")

    async def click_test_cases(self):
        await self.page.click("//div/ul/li/a[@href='/test_cases']")

    async def click_products(self):
        await self.page.click("//div/ul/li/a[@href='/products']")