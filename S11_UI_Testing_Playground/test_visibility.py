'''
Herem, we will learn about visibility of elements in Playwright.
Checking if an element is visible on screen mayb not be a trivial task.
We will learn about different ways an element can be hidden, and how to check for it.

an element can be 
1. Removed
2. Have zero width or height
3. Overlapped by another element 
4. Have opacity set to 0, 
5. Visibility set to hidden, 
6. Display set to none
7. Moved offscreen.

'''
import pytest
from utilis.is_element_overlapped import is_locator_overlapped
from playwright.sync_api import Page, expect, TimeoutError


def test_visibility(page: Page):
    page.goto("http://uitestingplayground.com/visibility")

    # Hide button
    hide_button = page.get_by_role("button", name="Hide")

    # other buttons
    removed_button = page.get_by_role("button", name="Removed")
    zero_width_button = page.get_by_role("button", name="Zero Width")
    overlapped_button = page.get_by_role("button", name="Overlapped")
    opacity_0_button = page.get_by_role("button", name="Opacity 0")
    hidden_button = page.get_by_role("button", name="Visibility Hidden")
    display_none_button = page.get_by_role("button", name="Display None")
    offscreen_button = page.get_by_role("button", name="Offscreen")

    # hide all the buttons
    hide_button.click()

    '''
     to_be_hidden() method does not specifically check if the element is removed from the DOM, 
     it will return True if element is not in the DOM
     or if
     CSS: display: none, visibility: hidden, opacity: 0
     HTML attribute: hidden
    '''

    # 1. Removed from DOM
    # Course Anwer
    # expect(removed_button).to_be_hidden()
    # to check if an element is removed from the DOM, we can use the to_be_attached() method
    expect(removed_button).not_to_be_attached()

    # 2. Zero width/height
    expect(zero_width_button).to_have_css("width", "0px")

    # 3. Overlapped by other element
    '''
    The course worked with the option to click and wait for timeout, 
    I felt like this isn't the best way to check for overlapped elements.
    I can use a JS evaluation to check if the element is overlapped by another element.
    I wrote a dedicated function for this in the utils folder.
    '''
    # Course answer
    # with pytest.raises(TimeoutError):
    #     overlapped_button.click(timeout=2000)

    # My Answer
    assert is_locator_overlapped(overlapped_button), "The button is not overlapped by another element"

    # 4. Opacity set to 0
    expect(opacity_0_button).to_have_css("opacity", "0")

    # 5. Visibility set to hidden
    expect(hidden_button).to_be_hidden()
    # expect(hidden_button).to_have_css("visibility", "hidden")

    # 6. Display set to none
    expect(display_none_button).to_be_hidden()
    # expect(display_none_button).to_have_css("display", "none")

    # 7. Moved offscreen
    expect(offscreen_button).not_to_be_in_viewport()