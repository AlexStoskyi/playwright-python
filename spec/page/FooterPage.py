from playwright.async_api import Page

class FooterPage:
    def __init__(self, page: Page):
        self.page = page

    async def scroll_to_footer(self):
        await self.page.evaluate("window.scrollTo(0, document.body.scrollHeight)")

    async def is_subscription_text_visible(self) -> bool:
        return await self.page.is_visible("//div[@class='single-widget']/h2")

    async def enter_email_and_submit(self, email: str):
        await self.page.fill("//form/input[@type='email']", email)
        await self.page.click("//form/button")

    async def is_success_message_visible(self) -> bool:
        return await self.page.is_visible("//div[@class='alert-success alert']")
