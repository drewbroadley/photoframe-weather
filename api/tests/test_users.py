import uuid
from django.core.urlresolvers import reverse

from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.test import APIClient

from api_partial_authentication.oauth_consumer.models import Consumer
from api_partial_authentication.tokens import JWTTokenManager


class UsersAPITests(APITestCase):

    def setUp(self):

        # Create mock user
        self.test_user = Consumer(
            id=str(uuid.uuid4()),
            type=Consumer.TYPE_USER
        )

        # Create valid token
        self.token = JWTTokenManager.generate_test_token(options={
            'uid': self.test_user.pk,
            'scopes': JWTTokenManager._compress_scopes(['read:users:self', 'write:users:self']),
            'trusted_application': False,
            'grant_type': "password"
        })

        super(UsersAPITests, self).setUp()

    def test_token(self):
        """
        Check false token header response
        """
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='Token ' + self.token)
        response = client.get('/v1/users/me/')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        client.credentials(HTTP_AUTHORIZATION='Bearer Blub')
        response = client.get('/v1/users/me/')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)
        response = client.get('/v1/users/me/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_user_v1(self):
        """
        Ensure we can get a user from test token.
        """
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)

        response = client.get('/v1/users/me/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsNotNone(response.data.get('user', None))
        user = response.data.get('user')

        self.assertEqual(user.get('id'), self.test_user.id)
        self.assertEqual(user.get('type'), Consumer.TYPE_USER)
