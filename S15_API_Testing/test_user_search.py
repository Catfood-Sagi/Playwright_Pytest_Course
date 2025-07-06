import pytest
from playwright.sync_api import *


@pytest.fixture
def api_context(playwright: Playwright) -> APIRequestContext:
    api_context = playwright.request.new_context(
        base_url="https://dummyjson.com"
    )
    yield api_context
    api_context.dispose()


def test_users_search(api_context: APIRequestContext):
    query = "John"
    response = api_context.get(f"/users/search?q={query}")

    users_data = response.json()

    print("Users found:", users_data["total"])

    for user in users_data["users"]:
        print("Checking user:", user["lastName"])
        assert any(query in user["lastName"] for user in users_data["users"])  # This will check that at least one of the  users has 'John' in the lastName
        # i had to make some changes becuase the return JSON when the course was written had changed
