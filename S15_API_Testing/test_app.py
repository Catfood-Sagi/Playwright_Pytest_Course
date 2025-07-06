import json
from pprint import pprint
from playwright.sync_api import *


def test_users_api(page: Page):
    response = page.goto("https://dummyjson.com/users/1") # goto uses GET by default

    # user_data = json.loads(response.body) # loads - load string
    ''' same thing can be done by using the built in'''
    user_data=response.json()

    print(json.dumps(user_data, indent=4)) #- using json.dumps with indent will make the json output to keep it structure for better readability

    # Asserting presenece of specific attributes
    assert "firstName" in user_data
    assert "lastName" in user_data

    # Asserting attributes values
    assert user_data["FfirstName"] == "Emily"
    assert user_data["lastName"] == "Johnson"




