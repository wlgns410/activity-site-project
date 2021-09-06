import json

from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model

from rest_framework.test import APITestCase
from rest_framework_jwt.settings import api_settings


User = get_user_model()

class SignUpTest(APITestCase):

    signup_url = "http://127.0.0.1:8000/users/signup"

    def test_signupview_post_user_registration_success(self):
        user_data = {
            "profile_url" : "file:///Users/jihoon/Desktop/git_commit_-m__Jihoon_Resume_%20(2).png",
            "password" : "12345678",
            "name" : "testuser",
            "email" : "wlgns410@gmail.com",
        }
        response = self.client.post(self.signup_url, data=user_data)
        self.assertEqual(201, response.status_code)

    def test_signupview_post_invalid_password(self):
        user_data = {
            "profile_url" : "file:///Users/jihoon/Desktop/git_commit_-m__Jihoon_Resume_%20(2).png",
            "password" : "1234567",
            "name" : "testuser",
            "email" : "wlgns410@gmail.com",
        }
        response = self.client.post(self.signup_url, data=user_data)
        self.assertEqual(400, response.status_code)

    def test_signupview_post_duplicated_email(self):
        exist_user_data = {
            "profile_url" : "file:///Users/jihoon/Desktop/git_commit_-m__Jihoon_Resume_%20(2).png",
            "password" : "12345678",
            "name" : "testuser",
            "email" : "wlgns410@gmail.com",
        }
        response = self.client.post(self.signup_url, exist_user_data)
        self.assertEqual(201, response.status_code)

        new_user_data = {
            "profile_url" : "file:///Users/jihoon/Desktop/git_commit_-m__Jihoon_Resume_%20(2).png",
            "password" : "12345678",
            "name" : "testuser",
            "email" : "wlgns410@gmail.com",
        }
        response = self.client.post(self.signup_url, new_user_data)
        self.assertEqual(400, response.status_code)

    def test_signupview_post_keyerror_email(self):
        user_data = {
            "profile_url" : "file:///Users/jihoon/Desktop/git_commit_-m__Jihoon_Resume_%20(2).png",
            "password" : "12345678",
            "name" : "testuser",
        }
        response = self.client.post(self.signup_url, data=user_data)
        self.assertEqual(400, response.status_code)

JWT_PAYLOAD_HANDLER = api_settings.JWT_PAYLOAD_HANDLER
JWT_ENCODE_HANDLER = api_settings.JWT_ENCODE_HANDLER


class SignInTest(APITestCase):

    signin_url = "http://127.0.0.1:8000/users/signin"

    def setUp(self):
        self.user = User.objects.create_user(
            profile_url = "file:///Users/jihoon/Desktop/git_commit_-m__Jihoon_Resume_%20(2).png",
            password = "12345678",
            name = "testuser",
            email = "wlgns410@gmail.com",)
        self.authentication = authenticate(
            profile_url = "file:///Users/jihoon/Desktop/git_commit_-m__Jihoon_Resume_%20(2).png",
            password = "12345678",
            name = "testuser",
            email = "wlgns410@gmail.com",
        )

    def tearDown(self):
        self.user.delete()

    def test_signinview_post_success(self):
        user_data = {
            "email" : "wlgns410@gmail.com",
            "password" : "12345678",
        }

        payload = JWT_PAYLOAD_HANDLER(self.authentication)
        jwt_token = JWT_ENCODE_HANDLER(payload)
        response = self.client.post(self.signin_url, data=user_data)

        self.assertEqual(200, response.status_code)
        self.assertTrue(response.json(), 
            {
                "message": "SUCCESS",
                "name" : "testuser",
                "token": jwt_token
            }
        )
    
    def test_signinview_post_password_does_not_match(self):
        user_data = {
            "email" : "wlgns410@gmail.com",
            "password" : "1234567",
        }
        response = self.client.post(self.signin_url, data=user_data)
        self.assertEqual(400, response.status_code)
    
    def test_signinview_post_user_does_not_exists(self):
        user_data = {
            "email" : "w@gmail.com",
            "password" : "12345678",
        }
        response = self.client.post(self.signin_url, data=user_data)
        self.assertEqual(400, response.status_code)

    def test_signinview_post_keyerror_email(self):
        user_data = {
            "password" : "12345678"
        }
        response = self.client.post(self.signin_url, data=user_data)
        self.assertEqual(400, response.status_code)
        
    def test_signinview_post_keyerror_password(self):
        user_data = {
            "email" : "wlgns410@gmail.com",
        }
        response = self.client.post(self.signin_url, data=user_data)
        self.assertEqual(400, response.status_code)
