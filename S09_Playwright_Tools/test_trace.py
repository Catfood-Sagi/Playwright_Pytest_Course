import pytest
from playwright.sync_api import BrowserContext, Page

DOCS_URL = "https://playwright.dev/python/docs/intro"


@pytest.fixture(autouse=True)
def trace_test(context: BrowserContext):
    # the (context: BrowserContext) is not manadatory, it just help # to understand that this fixture 
    # is used with the browser context

    # start tracing
    context.tracing.start(
        name="playwright", # name of the trace
        screenshots=True, # we can see screenshots frame by frame
        snapshots=True,   #
        sources=True,     # soucre code of each action
    )
    # pause until test function finishes
    yield
    # stop tracing and save it - Playwright a file muse be saved as a zip file
    context.tracing.stop(path="trace.zip")


# def test_page_has_get_started_link(page: Page):
#     page.goto("https://playwright.dev/python")

#     link = page.get_by_role("link", name="GET STARTED")
#     link.click()
    
#     assert page.url == DOCS_URL