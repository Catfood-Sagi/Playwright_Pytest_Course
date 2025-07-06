'''
Handlind the response

'''
from playwright.sync_api import Page, expect, Request, Response, Route

# defining on_request func
def on_route(route: Route):
    # Customising the response with out own HTML response body and status code
    # route.fulfill(
    #     status=200,
    #     body="<html><body><h1>Custome Response!</h1></body></html>",
    # )  

    # What if we wanted to get the actual response, and modify the same
    response = route.fetch()
    body = response.text().replace(
        " enables reliable end-to-end testing for modern web apps.",
        " is a great framework for web automation!"
    )

    route.fulfill(
        response=response,
        body=body,
    )


def test_docs_link(page: Page):
    page.route(
        "http://playwright.dev/python", on_route
    )

    page.goto("http://playwright.dev/python")
    page.pause()



