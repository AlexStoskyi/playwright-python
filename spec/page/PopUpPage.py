from playwright.async_api import Page

class PopUpPage:
    def __init__(self, page: Page):
        self.page = page

    async def pop_up(self):
        await self.page.wait_for_selector(  '//div[@class="fc-dialog-scrollable-content"]', timeout=5000)

    async def pop_up_confirm_button(self):
        await self.page.click('//div[@class="fc-button-background"]')




