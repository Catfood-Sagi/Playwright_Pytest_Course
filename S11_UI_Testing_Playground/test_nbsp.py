'''
NBSP - Non-Breaking Space
It's a special kind of space character that prevents line breaks at its position — unlike a normal space ( ), which allows wrapping.
In technical terms:
* HTML entity: &nbsp;
* Unicode code: U+00A0
'''
import pytest
from playwright.sync_api import Page, TimeoutError


def test_nbsp(page: Page):
    page.goto("http://uitestingplayground.com/nbsp")
    
    # using normal space
    with pytest.raises(TimeoutError):
        page.locator("//button[text()='My Button']").click(
            timeout=2000
        )
    # using non-breaking space
    page.locator("//button[text()='My\u00a0Button']").click()

    '''
    There is a "safe" way to check if an element is clickable
    beside checking first both 'to_be_visible()' + to_be_enabled()
    We can use the click(trail=True) 
    Tries to click the element without performing the action - trial=True is non-destructive — it wontt actually click
    (Just checks if it's visible, stable, and not blocked/obstructed)
    and it can be combined with assert
    assert locator.click(trial=True) is None  # Success = no error raised
    '''