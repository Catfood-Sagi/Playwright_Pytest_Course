'''
Handling a case when you need to scroll to see the element but part of it is already in viewport
in such case the scroll_into_view_if_needed() method WILL NOT WORK!
in such cases we will need to manually hover over the scroll area and use the mouse wheel 
to scroll the element into view

bounding_box() - gives the coordinates relative to the full page
is_visible, checks if the element in the DOM, not hidden, not display: none, has visible size, and within the viewport?"
'''
from utilis.scroll_to_element import scroll_to_element3
from playwright.sync_api import Page, expect


def test_overlapped(page: Page):
    page.goto("http://uitestingplayground.com/overlapped")
    
    input = page.get_by_placeholder("Name")

    # mouse-over scroll area
    div = input.locator("..") 
    # What we are doing here is basiclly locating the input element parent
    # (.) - is the same element
    # (..) - is the paraent
    div.hover()

    # Course Answer
    # scroll by 200 pixels horizontally
    page.mouse.wheel(0, 200)
    '''
    The page.mouse.wheel(x, y) method scrolls by the given amounts, meaning:
    x = how many pixels to scroll horizontally (positive = right, negative = left)
    y = how many pixels to scroll vertically (positive = down, negative = up)

    I didn't like it so i wrote a utili function 'scroll_to_element' instead of blindly scrolling an x amount up/down left/right
    UPDATE:
    my util didn't work as intended
    '''

    # My Answer
    # scroll_to_element3(input)

    # fill data
    data = "python"
    input.fill(data)

    # take screenshot of scroll-area
    div.screenshot(path="test-overlapped.jpg")

    expect(input).to_have_value(data)

    