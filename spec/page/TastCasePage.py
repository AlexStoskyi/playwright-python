# spec/page/test_cases_page.py
from playwright.async_api import Page

class TestCasesPage:
    def __init__(self, page: Page):
        self.page = page

    async def is_test_cases_page_visible(self):
        return await self.page.title() == "Test Cases - Automation Exercise"

    async def title_is_visible(self):
        return await self.page.is_visible("//div/h2[@class='title text-center']")