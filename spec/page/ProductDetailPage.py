# spec/page/product_detail_page.py
from playwright.async_api import Page

class ProductDetailPage:
    def __init__(self, page: Page):
        self.page = page

    async def is_product_detail_visible(self):
        return await self.page.is_visible("//div[@class='product-information']")

    async def get_product_details(self):
        name = await self.page.inner_text("//div[@class='product-information']/h2")
        category = await self.page.inner_text("//div[@class='product-information']/p[@xpath='1']")
        price = await self.page.inner_text("//div[@class='product-information']/span/span")
        availability = await self.page.inner_text("(//div[@class='product-information']/p/b)[1]")
        condition = await self.page.inner_text("(//div[@class='product-information']/p/b)[2]")
        brand = await self.page.inner_text("(//div[@class='product-information']/p/b)[3]")
        return {
            "name": name,
            "category": category,
            "price": price,
            "availability": availability,
            "condition": condition,
            "brand": brand
        }
