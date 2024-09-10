import pytest
from playwright.sync_api import sync_playwright
import allure
from allure_commons.types import AttachmentType

# Fixture for browser setup
@pytest.fixture(scope="function", params=["chromium", "firefox", "webkit"])
def browser(request):
    playwright = sync_playwright().start()
    browser = getattr(playwright, request.param).launch(headless=True)
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()
    browser.close()
    playwright.stop()

# Hook for taking screenshots on test failure
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    # Check if the test has failed
    if report.when == "call" and report.failed:
        # Check if the browser fixture is available
        if 'browser' in item.funcargs:
            page = item.funcargs['browser']
            # Attach a screenshot of the page
            allure.attach(page.screenshot(), name="Failed test screenshot", attachment_type=AttachmentType.PNG)
