'''
There are plent of ways to check text on the page.
You can check if the text is present, contains some text, or matches a regex.  
You can also check if the text is exact or contains some text.
'''
from playwright.sync_api import Page, expect


def test_get_started_link(page: Page):
    page.goto("https://playwright.dev/python")

    # locating the dropdown menu
    dropdown_menu = page.locator("ul.dropdown__menu")
    # contains text
    expect(dropdown_menu).to_have_text("Python")
    expect(dropdown_menu).to_contain_text("Node.js")
    expect(dropdown_menu).to_contain_text("Java")
    expect(dropdown_menu).to_contain_text(".NET")

    # # exact text
    heading  = page.locator("h1.hero__title")

    expect(heading).to_have_text("Playwright enables reliable end-to-end testing for modern web apps.")