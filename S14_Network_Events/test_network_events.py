'''
When we navifate to a website, we send a request to a URL that is the website
when the website gets the request, it sends us a response back which is the HTML code or other resource files like CSS or any image

To handle these event, we can set up an event listener, we we learn in previous sections
to set an event listener for the request event we can use the page object 'on()' method.and the even ehich is 'request' and set up a function which will be called
'''

from playwright.sync_api import Page, expect, Request, Response

# defining on_request func
def on_request(request: Request):
    print("Sent Request: ", request)

def on_response(response: Response):
    print("Received Response: ", response)

def test_docs_link(page: Page):
    page.on("request", on_request)
    page.on("response", on_response)

    page.goto("http://playwright.dev/python")

    docks_link = page.get_by_role("link", name="Docs")
    docks_link.click()

    expect(page).to_have_url(
        "https://playwright.dev/python/docs/intro"
    )