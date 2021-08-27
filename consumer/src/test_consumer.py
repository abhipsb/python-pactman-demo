"""pact test for consumer"""

import pytest
import atexit
import unittest
import requests
from pactman import Consumer, Provider, Like
from consumer import UserConsumer


pact = Consumer('Consumer').has_pact_with(Provider('Provider'))
#print('start service')
#pact.start_service()
#atexit.register(pact.stop_service)
consumer_service = UserConsumer(pact.uri)

class ContractTesting(unittest.TestCase):
    def test_non_existing_get_user(self):
        (pact
        .given('UserB does not exist')
        .upon_receiving('a request for UserB')
        .with_request('get', '/users/UserB')
        .will_respond_with(404))

        with pact:
            result = consumer_service.get_user('UserB')
            self.assertEqual(result, None)
            pact.verify()

    def test_existing_get_user(self):
        expected = { 'name': 'UserA' }

        (pact
        .given('UserA exists')
        .upon_receiving('a request for UserA')
        .with_request('get', '/users/UserA')
        .will_respond_with(200, body=Like(expected)))

        with pact:
            user = consumer_service.get_user('UserA')
            self.assertEqual(user.name, 'UserA')
            pact.verify()