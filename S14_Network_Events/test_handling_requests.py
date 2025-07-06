'''
How to handle request

We can read different properties of our request along with all other attributes
like request.url - the url it was sent to
request.post_data and post_data_json

what we cannot do here, is modifying or change the request in anyway, a listenr cannot do that
what we need is to use ROUTE HANDLER

The route method, takes the URL which will be used to handle.
The route object is the page navigation object.
it is the state of the navigation which has our request with some addtional functionality to control our navigation
For Example:
* Continue it
* Cancel it

'''
from playwright.sync_api import Page, expect, Request, Response, Route

def on_route(route: Route):
    # route.request.post_data = "data" # we can cutome to post data beind sent
    # route.continue_() # This will just continue
    print("Request aborted", route.request)
    route.abort() # This will cancel the navigation


def test_docs_link(page: Page):
    # Instead of listeners
    # page.on("request", on_request)
    # page.on("response", on_response)

    # we will use the route method
    # page.route("https://playwright.dev/python/img/playwright-logo.svg", on_route) # When the page object request to this URL it will trigger the on_route and abort it

    ''' What if we wanted to skip all of the images
    we can about all requests for image that ends with PNG
    this is done by URL Matching
    so this URL - page.route("https://playwright.dev/python/img/playwright-logo.svg", on_route)
    Becomes
    '''
    # page.route("https://*/python/img/playwright-logo.svg", on_route) # a single * matches any single part (but not across / by default)
    ''' OR '''
    # (page.route("**/playwright-logo.svg", on_route)) # double * matches everything, including slashes //

    # Another example
    page.route("**/*.{png,jpg,jpeg}", on_route) # will abort the mentioned images requests

    '''
    This can also be done by modifying our page.route to page.route(**) - which is EVERYTHING
    and our on_route function to
    if route.request.resource_type == "image"
        route.abort()
    else route.continue_()
    '''

    
    page.goto("http://playwright.dev/python")

    page.screenshot(path="playwright.jpg", full_page=True)

