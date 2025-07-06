from playwright.sync_api import sync_playwright
from time import perf_counter

def on_load(page):
    print("Page loaded successfully!", page)

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(
        headless=False, slow_mo=500
    )
    page = browser.new_page()
    # Register the load event listener
    page.on("load", on_load) # This will trigger when the page is fully loaded
    page.goto("https://bootswatch.com/default")

''' We can listen to different events like:
    page.on("load", on_load) # Page loaded
    page.on("filechooser", on_load) # File chooser opened
    page.on("domcontentloaded", on_load) # DOM content loaded
    page.on("request", on_load) # Request made
    page.on("response", on_load) # Response received
    page.on("console", on_load) # Console message
    page.on("error", on_load) # Error occurred
    page.on("pageerror", on_load) # Page error
    page.on("close", on_load) # Page closed
    page.on("dialog", on_load) # Dialog opened
    page.on("requestfinished", on_load) # Request finished
    page.on("requestfailed", on_load) # Request failed
    page.on("websocket", on_load) # WebSocket opened 
    and so forth.'''
    
browser.close()