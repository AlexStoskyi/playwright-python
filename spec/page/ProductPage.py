# spec/page/products_page.py
from playwright.async_api import Page


class ProductPage:
    def __init__(self, page: Page):
        self.page = page

    async def is_products_page_visible(self):
        return await self.page.is_visible("//div[@class='features_items']/h2")

    async def is_products_list_visible(self):
        return await self.page.is_visible("//div[@class='col-sm-9 padding-right']")

    async def click_first_product_view_button(self):
        await self.page.click("(//div[@class='choose'])[1]")

    async def enter_search_query(self, query: str):
        await self.page.fill("//input[@id='search_product']", query)

    async def click_search_button(self):
        await self.page.click("//button[@id='submit_search']")

    async def is_searched_products_visible(self):
        return await self.page.is_visible("//div[@class='features_items']/h2")

    async def are_searched_products_visible(self):
        return await self.page.is_visible("//div[@class='productinfo text-center']")

    async def search_name_is_the_same(self, search_name: str) -> bool:

        product_elements = await self.page.query_selector_all("//div[@class='productinfo text-center']/p")

        for element in product_elements:
            text = await element.inner_text()
            if search_name.lower() not in text.lower():
                return False
        return True