'''
Scrolling an element into view before interacting with it.
This is useful when the element is not visible in the viewport.
this is done using the scroll_into_view_if_needed() method.
'''
from utilis.element_in_viewport import is_fully_visible
from playwright.sync_api import Page


def test_scrollbars(page: Page):
    page.goto("http://uitestingplayground.com/scrollbars")
    
    btn = page.get_by_role("button", name="Hiding Button")


    btn.scroll_into_view_if_needed()

    # clicking an element automatically brings the element into view,
    # btn.click()

    '''There isn't a built-in way to check if an element is in the viewport,
    but we can use a custom function to check for ir using the bounding box.
    '''
    assert is_fully_visible(btn) 

    page.screenshot(path="test-scrollbars.jpg")