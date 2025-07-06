import os
import json
from playwright.sync_api import sync_playwright

chrome_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
user_data_dir = "C:\\Users\\sagig\\playwright-user-data-clean"
with sync_playwright() as playwright:

    browser = playwright.chromium.launch_persistent_context(
        user_data_dir=user_data_dir,
        executable_path=chrome_path,
        headless=False, 
        slow_mo=2000,
        args=["--disable-blink-features=AutomationControlled"]
        )
    
    page = browser.pages[0] if browser.pages else browser.new_page()
    page.goto("https://accounts.google.com/")

    page.pause()
    
    storage_state = browser.storage_state()
    with open("C:/Users/sagig/venv/playwright/.auth/storage_state.json", "w") as f:
        json.dump(storage_state, f, indent=2)

    browser.close()
   