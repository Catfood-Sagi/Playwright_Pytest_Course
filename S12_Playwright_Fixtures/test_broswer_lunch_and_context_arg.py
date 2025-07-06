'''
When we use the 'Browser' fixture, we dont get to configure its launch options
The same goes for our new context - we cannot define the arguments which are used to create the same

In this lesson we will learn how to pass arguments when we launch our browser
and create new context.

the fixture we will use will return the arguments as a dictionary.
this fixture will be a session scope fixture
'''
import pytest
from playwright.sync_api import Page, expect

@pytest.fixture(scope="session")
#def broweser_type_launch_args(): # when doing it like this, i will need to also add them to the run command
def browser_type_launch_args(browser_type_launch_args):
    return {
        **browser_type_launch_args,
        "headless": False,
        "slow_mo": 500,
    }

def test_page_has_docs_link(page: Page):
    page.goto("http://playwright.dev/python")

    docs_link = page.get_by_role("link", name="Docs")

    expect(docs_link).to_be_visible()