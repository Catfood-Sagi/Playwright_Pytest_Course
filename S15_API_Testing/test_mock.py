'''
Mocking is a powerful technique in API testing that lets you simulate real API behavior without making actual network calls.
Itss especially useful when the real service is unavailable, unstable, or still under development.
By using mocks, you can test how your code handles various responses—success, errors, timeouts—in a controlled and repeatable way.
This helps keep tests fast, reliable, and independent of external systems.
In the example below, we will demonstrate how to mock an API response using Python to ensure your application logic behaves correctly.

'''

'''website performs navigation. And in the process, it makes an API call that is requesting data from the API'''
from playwright.sync_api import *
import json

# This is a "Pure" Mocking - we are not hittin the real endpoint

def on_api_call(route: Route):
    # will return our request with the provided data
    route.fulfill(
        json={
            "firstName": "Sagi",
            "lastName": "Gez"
        }
    )

def test_user_api(page: Page):
    USERS_API_URL = "https://dummyjson.com/users/1"

    # initiate the API call with the navifation
    page.route(USERS_API_URL, on_api_call)

    response = page.goto(USERS_API_URL)

    print("Got Data: ", response.json())

''' after writing this code, we can remove the page.route just to see what we would have gotten
    That is, all the data that is initial in the server (data about Emily Johnson)
    
    That's is how we can go a head and provide a smaple data to an API call using the route handler
    
    We can also provide or change the data returned from the API - instead of providing hard coded calue like I just did using the fulfill method
    
    What we can do is to fetch the response first and then modify the data in it'''

# While this can also be considerd 'mocking' it's more of an mock & modify, we are altering the response but still hiting the real API.
def on_api_call(route: Route):
    # will return our request with the provided data
    response = route.fetch()
    user_data = response.json()
    user_data["lastName"] = "David"
    user_data["age"] = 20

    # now we take our custome data back to our request using fulfill
    # because we have the response, we can provide it back as well and override the JSON data

    route.fulfill(
        response=response, # resoibse is what we fetch
        json=user_data,     # the JSON is our custome data
    )

def test_user_api(page: Page):
    USERS_API_URL = "https://dummyjson.com/users/1"

# initiate the API call with the navifation
    page.route(USERS_API_URL, on_api_call)

    response = page.goto(USERS_API_URL)

    print("Got Data: ", response.json())

''' this is how you can mock an api to provide it with sample data or change the actual data'''