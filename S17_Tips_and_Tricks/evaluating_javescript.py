'''
Executing JavaScript in our Python script is an important tool
when we want to run the code on the website isteld - this can only be done with JavaScript

This is the same as running JavaScript code in the Console tab (DevTools)

Example:
opening the Console and writing
window.scrollBy(0, 400)  - will scroll down 400 pixel
if we want to scroll till the end of the page
we can use the 'document' (out HTML document) .body (HTML bodyy) and the scrollHeight - this will give us the over all pixel of the page 

window.scrollBy(0, document.body.scrollHeight)

Now, to do it on our Python script, we will need to use the 'evalute' method

'''

import pytest
from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    browser = playwright.chromium.launch()

    page = browser.new_page()
    page.goto("https://playwright.dev/python")
    page.evaluate("window.scrollBy(0,900)")

    # Using evalute to run JavaScript
    # Evalute let you write JavaScript as a string
    #page.evaluate("window.scrollBy(0, document.body.scrollHeight)") # Same code we ran in the console

    page.screenshot(path="end_of_page.jpg")

