# pylint: disable=redefined-outer-name
"""
Example of using the users API
"""

import os
import sys
import logging
from typing import Tuple
from kentik_api import kentik_api
from kentik_api.public.user import User

logging.basicConfig(level=logging.INFO)


def get_auth_email_token() -> Tuple[str, str]:
    try:
        email = os.environ['KTAPI_AUTH_EMAIL']
        token = os.environ['KTAPI_AUTH_TOKEN']
        return email, token
    except KeyError:
        print('You have to specify KTAPI_AUTH_EMAIL and KTAPI_AUTH_TOKEN first')
        sys.exit(1)


def run_crud():
    """
    Runs example CRUD API calls and prints responses
    """

    email, token = get_auth_email_token()
    client = kentik_api.for_com_domain(email, token)

    print("### CREATE")
    user = User(username='test_user', full_name='Test User', email='test@user.example', role='Member',
                password='test_password', email_service=True, email_product=True)
    created = client.users.create(user)
    print(created.__dict__)
    print()

    print("### GET_ALL")
    got = client.users.get_all()
    for i in got:
        print(i.__dict__)
    print()

    print("### UPDATE")
    user = User(id=created.id,
                full_name='User Testing',
                )
    got = client.users.update(user)
    print(got.__dict__)
    print()

    print("### GET")
    got = client.users.get(created.id)
    print(got.__dict__)
    print()
    
    print("### DELETE")
    deleted = client.users.delete(created.id)
    print(deleted)


if __name__ == "__main__":
    run_crud()
