from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    # Launch the browser
    browser = playwright.chromium.launch(headless=False,slow_mo=500)
    #Create a new page
    page = browser.new_page()
    #Visit the playwright website
    page.goto("https://bootswatch.com/default")

    # Locate a link element with the text "Docs"
    button = page.get_by_role('button', name='Primary').first
    button.click()

    # Get the URL
    browser.close()