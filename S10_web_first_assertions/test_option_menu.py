'''
How to check that a select/option menu has the expected value(s).
'''

from playwright.sync_api import Page, expect


def test_app(page: Page):
    page.goto("https://bootswatch.com/default")
    
    option_menu = page.get_by_label("Example select")
    
    # expect selected option
    expect(option_menu).to_have_value("1")

    multi_option_menu = page.get_by_role("listbox", name="Example multiple select")
    multi_option_menu.select_option(["2", "4"])


    # expect selected options
    expect(multi_option_menu).to_have_values(["2", "4"])
    '''It might seem abit strange but its important to remember that 'to_have_values
    is checking the current selected values in the multi-option menu.
    so if i wanted to assert that by default, not option is selected,
    i could use to_have_values([])'''
    

    '''
    If i wanted to assert the visibilty of all the options in the multi-option menu,
    i could use the following code:
    expect(multi_option_menu.locator("option")).to_have_text(["1", "2", "3", "4", "5"])
    

    '''