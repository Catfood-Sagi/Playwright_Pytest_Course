from playwright.sync_api import sync_playwright


with sync_playwright() as playwright:

    browser = playwright.chromium.launch(headless=False, slow_mo=1000)

    # This is how you load an authentication state from a file.
    # This is useful for reusing authentication state across different sessions.
    context = browser.new_context(
        storage_state="playwright/.auth/storage_state.json"
    )
    
    page = context.new_page()
    page.goto("https://accounts.google.com/")

    page.pause() 
    
    context.close()

'''
context.new_page() is preferred over browser.new_page() because:
A browser context acts like a separate browser profile.
When you use context.new_page(), all the pages opened under that context:

    * Share the same cookies
    * Share the same local storage
    * Share the same storage_state if one is loaded

This makes it perfect for scenarios like:
1. Logged-in user sessions
2. Isolated tests that shouldn't interfere with each other
'''