from dotenv import load_dotenv
import os
load_dotenv()
PASSWORD=os.getenv("PASSWORD")
EMAIL = os.getenv("EMAIL")
from playwright.sync_api import sync_playwright

# with sync_playwright() as playwright:

#     browser = playwright.chromium.launch(headless=False, slow_mo=1000)
#     page = browser.new_page()
#     page.goto("https://accounts.google.com")  
#     email_input = page.get_by_label("Email or phone")
#     email_input.fill("sagigez@gmail.com")

#     next_btn = page.get_by_role("button", name="Next")
#     next_btn.click()

#     password_input = page.get_by_label("Enter your password")
#     password_input.fill(PASSWORD)  # Replace with your actual password

# --------------------------------------------

with sync_playwright() as playwright:

    browser = playwright.chromium.launch(headless=False, slow_mo=2000)
    context = browser.new_context()
    
    page = context.new_page()
    page.goto("https://accounts.google.com/")
    
    #Enter email
    email_input = page.get_by_label("Email or phone")
    email_input.fill(EMAIL)

    page.get_by_role("button", name="Next").click()

    # Enter possword
    password_input = page.get_by_role("input", name="Passwd")
    password_input.fill(PASSWORD)

    page.get_by_role("button", name="Next").click()

    # In case of 2FA, we will need to  handle that manually
    page.pause()  # Pause to allow for manual 2FA input if needed

    # save authentication state
    context.storage_state(
        path="playwright/.auth/storage_state.json"
        )
    context.close()

