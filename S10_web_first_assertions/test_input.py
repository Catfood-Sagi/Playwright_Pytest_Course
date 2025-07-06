'''
expecting diiferent state of input field.
first we'll make sure its hidden (before clicking it), then visible/editable, and finally check its value after filling it.

the search is a button that opens the input field, which is hidden initially.
in the web page, it says that you can also open it using Control+K (or Command+K on Mac).
when opening it we expect the input to be both visible/editable and empty.

Than we will type something in the input field and check that the value is as expected.
'''

from playwright.sync_api import Page, expect


def test_get_started_link(page: Page):
    page.goto("https://playwright.dev/python")
    input = page.get_by_placeholder("Search docs")

    # input is hidden initially
    expect(input).to_be_hidden()

    # search button
    search_btn = page.get_by_role("button", name="Search")
    # using press method instead of click
    search_btn.press("Control+KeyK") # should pop the search menu
    
    # input should be visible/editable
    expect(input).to_be_editable()
    # input should be empty initially
    expect(input).to_be_empty()

    # type some query in the input
    query = "assertions"
    input.fill(query)

    # expect the input value as query
    expect(input).to_have_value(query)