# from django.urls import reverse
# from rest_framework.test import APITestCase
# from users.models import User

# # Create your tests here.
# class ArticleCreateTest(APITestCase):
#     @classmethod
#     def setUpTestData(cls): # 더미데이터 classmethod로 생성
#         cls.user_data = {'username': 'john', 'password': 'johnpassword'}
#         cls.article_data = {'title': 'some title', 'content': 'some content'}
#         cls.user = User.objects.create_user('john', 'johnpassword')
    
#     def setUp(self):
#         self.access_token = self.client.post(reverse('token_obtain_pair'), self.user_data).data['access']   ## 엑세스 토큰을 받아옴
    
    
    
#     def test_fail_if_not_logged_in(self): # 로그인 하지 않았을때 글 작성 테스트
#         url = reverse("article_view")
#         response = self.client.post(url, self.article_data)
#         self.assertEqual(response.status_code, 401)
        
     
#     def test_create_article(self): # 글 작성 테스트
#         response = self.client.post(
#             path=reverse("article_view"),
#             data=self.article_data,
#             HTTP_AUTHORIZATION=f"Bearer {self.access_token}"
#         )
#         self.assertEqual(response.data["message"], "글 작성 완료!!")
#         self.assertEqual(response.status_code, 200