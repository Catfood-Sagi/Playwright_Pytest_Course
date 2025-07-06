'''
Testing input field to make sure it can be filled and the button text is updated accordingly.
'''

from playwright.sync_api import Page, expect


def test_text_input(page: Page):
    page.goto("http://uitestingplayground.com/textinput")

    # text input value
    testing_text_input = "Testing test input"

    # fill value
    input = page.get_by_label("Set New Button Name")
    input.fill(testing_text_input)

    # click button
    btn = page.locator("button#updatingButton")
    btn.click()

    # expect button text to be input value
    expect(btn).to_have_text(testing_text_input)