'''
In modern applications, elements on the page can change dynamically, such as when a button is clicked or an API call is made.
Even the ID of an element can change, making it difficult to select the element using a static selector.

That's why its better to use method like get_by_role, get_by_label etc..

one of the most common ways to deal with dynamic attributes is the data testid attribute.
get_by_testid

'''
from playwright.sync_api import Page, expect


def test_dynamic_id(page: Page):
    page.goto("http://uitestingplayground.com/dynamicid")

    button = page.get_by_role(
        "button", name="Button with Dynamic ID"
    )
    expect(button).to_be_visible()

    button.click()
    page.get