'''
Working with elementes that change attributes when being hovered.
'''
from playwright.sync_api import Page, expect


def test_mouse_over(page: Page):
    page.goto("http://uitestingplayground.com/mouseover")
    
    click_link = page.get_by_title("Click me")
    click_link.hover()

    active_link = page.get_by_title("Active link")
    active_link.click(click_count=2)

    click_count = page.locator("span#clickCount")

    
    # I added this part for the second button in t he page.
    link_btn = page.get_by_title("Link Button")
    link_btn.hover()

    hovered_link_btn = page.locator('[onmouseleave = "linkButtonInactive(this)"]')
    hovered_link_btn.click()

    link_btn_click_count = page.locator("span#clickButtonCount")


    expect(link_btn_click_count).to_have_text("1")
    expect(click_count).to_have_text("2")

