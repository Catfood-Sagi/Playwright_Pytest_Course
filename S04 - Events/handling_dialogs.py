from playwright.sync_api import sync_playwright
from time import perf_counter

def on_dialog(dialog):
    # On dialog, you can either accept or dismiss it
    dialog.accept()  # Accept the dialog
    # dialog.dismiss()   Dismiss the dialog
    print("Dialog accepted", dialog)

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(
        headless=False, slow_mo=5000
    )
    page = browser.new_page()
    # Register the load event listener
    page.on("dialog", on_dialog) # This will trigger when the page is fully loaded
    page.goto("https://testpages.herokuapp.com/styled/alerts/alert-test.html")
    alert_btn = page.get_by_role("button", name="Show confirm box")
    alert_btn.click()

# On Alert box, there only one option, with the button "OK" so we can just use click
# On Prompt dialog box we can enter the content in the dialog.accept("Hello world!")