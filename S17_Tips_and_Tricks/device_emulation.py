from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False, slow_mo=500)

    # saving the pixel 5 dics to a dedicated var
    pixel_5_args = playwright.devices["Pixel 5"]

    # defining our context with the pixel 5 dict args
    context = browser.new_context(**pixel_5_args)  # the ** is Python way of unpacking a dict into keyword args which is what the context expect
    
    page = context.new_page()
    page.goto("https://playwright.dev/python")

    link = page.get_by_role("link", name="GET STARTED")
    link.click()
