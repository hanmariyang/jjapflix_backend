from django.urls import path, re_path, include
from django.contrib.auth import views as auth_views
from users import views
from dj_rest_auth.registration.views import VerifyEmailView

urlpatterns = [
    path('delete/', views.UserDeleteView.as_view(), name='user_view'),  #회원탈퇴
    path('<int:user_id>/', views.ProfileView.as_view(), name='profilw_view'), # 회원정보 조회
    path('dj-rest-auth/', include('dj_rest_auth.urls')),  # 로그인 및 기타 dj-rest-auth 기능
    path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')), #회원가입
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    re_path(r'^account-confirm-email/$', VerifyEmailView.as_view(), name='account_email_verification_sent'), #이메일 인증 
    re_path(r'^account-confirm-email/(?P<key>[-:\w]+)/$', views.ConfirmEmailView.as_view(), name='account_confirm_email'), # 이메일 인증

]