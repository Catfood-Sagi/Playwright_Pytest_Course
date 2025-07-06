'''
AJAX - an AJAX is a technique that allows web applications to send and receive data asynchronously
without interfering with the display and behavior of the existing page.
This means that you can update parts of a web page without reloading the whole page.

for example, you can load data from a server in the background and display it on the page without refreshing the page.
'''
from playwright.sync_api import Page, expect

def test_ajax(page):
    page.goto("http://uitestingplayground.com/ajax")
    ajax_btn = page.get_by_role("button", name="Button Triggering AJAX Request")
    ajax_btn.click()

    # Wait for the AJAX request to complete and the response to be displayed
    txt_content = page.locator("p.bg-success")
    txt_content.wait_for()

    expect(txt_content).to_be_visible()
