import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture
def page():
    # fixture that start Playright
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch()
    return browser.new_page()


