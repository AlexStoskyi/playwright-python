# pages/contact_us_page.py

class ContactUsPage:
    def __init__(self, page):
        self.page = page

    async def verify_contact_us_page(self):
        return await self.page.is_visible("//div[@class='col-sm-12']/h2")

    async def fill_contact_form(self, name, email, subject, message):
        await self.page.fill("input[name='name']", name)
        await self.page.fill("input[name='email']", email)
        await self.page.fill("input[name='subject']", subject)
        await self.page.fill("textarea[name='message']", message)

    async def upload_file(self, file_path):
        await self.page.set_input_files("//div[@class='form-group col-md-12']/input[@type='file']", file_path)

    async def click_submit(self):
        await self.page.click("//div/input[@data-qa='submit-button']")

    async def confirm_alert(self):
        self.page.once("dialog", lambda dialog: dialog.accept())

    async def verify_success_message(self, success_message):
            return await self.page.is_visible("//div[@class='status alert alert-success' and contains(text(), '{success_message}')]")

    async def click_home_button(self):
        await self.page.click("//a[contains(text(), 'Home')]")
