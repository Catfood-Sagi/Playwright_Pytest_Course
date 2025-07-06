'''

'''

from playwright.sync_api import *
import requests
import pytest
import json

import pytest
from playwright.sync_api import *


@pytest.fixture
def api_context(playwright: Playwright) -> APIRequestContext:
    api_context = playwright.request.new_context(
        base_url="https://dummyjson.com",
        extra_http_headers={'Content-Type': 'application/json'},
    )
    yield api_context
    
    api_context.dispose()


def test_create_user(api_context: APIRequestContext):
    response = api_context.post(
        "users/add",
        data={
            "firstName": "Damien",
            "lastName": "Smith",
            "age": 27
        }
    )
    user_data = response.json()
    #print(json.dumps(user_data, indent= 4))

    assert response.status == 201
    assert user_data["id"] == 209
    assert user_data["firstName"] == "Damien"


    ''' 
        This can also be done by using the fetch() method and providing the url, method
        headers and content

        assuming we still have the fixture

        api_context.fetch(
        "users/add",
        method = "POST,
        data={
            "firstName": "Damien",
            "lastName": "Smith",
            "age": 27
        })
    '''

def test_update_user(api_context: APIRequestContext):
    response = api_context.put(
        "users/2",
        data={
            "lastName": 'David',
            "gender": 'female'
        }
    )

    user_data = response.json()
    #print(json.dumps(user_data, indent= 4))
    assert user_data["lastName"] == "David"
    assert user_data["gender"] == "female"

def test_delete_user(api_context: APIRequestContext):
    response = api_context.delete(
        "users/2",
    )
    user_data = response.json()
    #print(json.dumps(user_data, indent= 4))
    assert user_data["id"] == 2
    assert user_data["isDeleted"] == True
    assert user_data["deletedOn"]
