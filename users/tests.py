from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from users.models import User

# Create your tests here.

class UserRegistrationTest(APITestCase):
    def test_registration(self):  #회원가입 테스트
        url = reverse("rest_register")   # url name
        user_data = {
                "email":"test@naver.com",
                "nickname":"junseok",
                "password1":"password123@",
                "password2":"password123@"
            }
        response = self.client.post(url, user_data)  # APITestCase의 기본적인 세팅
        self.assertEqual(response.status_code, 201)


class LoginUserTest(APITestCase):
    def setUp(self):  # DB 셋업
        
        self.data = {'email': 'test@naver.com', 'password': 'password123@'}
        self.user = User.objects.create_user('test@naver.com', 'password123@')
    
    def test_login(self):   # 로그인 테스트
        response = self.client.post(reverse('rest_login'), self.data)
        self.assertEqual(response.status_code, 200)
    
    # def test_get_user_data(self): # 유저정보 조회 테스트
    #     access_token = self.client.post(reverse('token_obtain_pair'), self.data).data['access']   ## 엑세스 토큰을 받아옴
    #     response = self.client.get(
    #         path=reverse("user_view"),
    #         HTTP_AUTHORIZATION=f"Bearer {access_token}"
    #     )
    #     # print(response.data)
    #     # self.assertEqual(response.status_code, 200)
    #     self.assertEqual(response.data['username'], self.data['username'])