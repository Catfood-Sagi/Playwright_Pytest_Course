'''

'''

from playwright.sync_api import Page, expect


def test_load_delay(page: Page):
    page.goto("http://uitestingplayground.com/")

    load_delay_link = page.get_by_role("link", name="Load Delay")
    load_delay_link.click()

    btn = page.get_by_role("button", name="Button Appearing After Delay")
    btn.wait_for() # Wait for the button to appear after the delay

    expect(btn).to_be_visible()