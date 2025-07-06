'''
To create an API context we required the Playwirhgt instance (adding the playwright fixture)
Using the context with the metod you want will improve predormance since it not initiating a browser.

the context can take different arguments
'''
from playwright.sync_api import *
import pytest

def test_users_api(playwright: Playwright):
    api_context = playwright.request.new_context(
        base_url="https://dummyjson.com"       # when ever i add a base url, when ever i sent a request i only need to provide the url after this point
    )

    response = api_context.get("/users/1") # will be append to the base url

    user_data = response.json()

    assert "firstName" in user_data
    assert "lastName" in user_data

    assert user_data["firstName"] == "Emily"
    assert user_data["lastName"] == "Johnson"

    api_context.dispose()  # Closing the context is important to free system resousces (Space and Memory)

''' Now we can extract this cycle and api context to a fixture so instead of the code here ^^above^^
    We will have this  '''

@pytest.fixture
#puting it in a fixture using yield will handle the setup and teardown
def api_context(playwright: Playwright):
        api_context = playwright.request.new_context(
        base_url="https://dummyjson.com"   
    )
        yield api_context
        api_context.dispose()


def test_users_api(api_context: APIRequestContext):

    response = api_context.get("/users/1") # will be append to the base url

    user_data = response.json()

    assert "firstName" in user_data
    assert "lastName" in user_data

    assert user_data["firstName"] == "Emily"
    assert user_data["lastName"] == "Johnson"
