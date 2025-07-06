from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    # Launch the browser
    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    # Create a new page
    page = browser.new_page()
    # Visit the Playwright website
    page.goto("https://bootswatch.com/default")
    page.screenshot(path="screenshot.png") # can add a full_page=True arg to cap entire page

    '''
    We can also take screenshots of specific elements:
    element.screenshot(path="element_screenshot.png")
    '''

    