from playwright_page import PlaywrightPage
from playwright.sync_api import Page, expect
import pytest

@pytest.fixture
def homepage(page):
    return PlaywrightPage(page)


def test_docs_link(homepage):
    homepage.visit_docs()

    expect(homepage.page).to_have_url(
        "https://playwright.dev/python/docs/intro"
    )


def test_docs_search(homepage):
    query = "assertions"

    homepage.search(query)

    expect(homepage.search_results()).to_contain_text(
        "List of assertions"
    )