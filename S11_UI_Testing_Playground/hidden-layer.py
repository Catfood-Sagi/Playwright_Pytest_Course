'''
Z - order stack refer to the layering of elements on a web page.
that means - what appears in front or behind other elements.

In this example, we will test a button that is hidden behind another element.
We want to make sure we can't click the initial button twice, as it is hidden behind another element.
'''


import pytest
from playwright.sync_api import TimeoutError, Page


def test_hidden_layer(page: Page):
    page.goto("http://uitestingplayground.com/hiddenlayers")

    green_btn = page.locator("button#greenButton")
    # click once
    green_btn.click()

    # Testing that clicking the button (greenButton) again will raise a TimeoutError
    # because the button is hidden behind another element (blueButton)
    with pytest.raises(TimeoutError):
        green_btn.click(timeout=2000)
