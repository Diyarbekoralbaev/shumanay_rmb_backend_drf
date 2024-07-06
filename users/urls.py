from django.urls import path
from .views import SignupView, LoginView, RefreshView, ProtectedView, MeView, ChangePasswordView, LogoutView, ForgotPasswordView, VerifyOTPView

urlpatterns = [
    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('login/refresh/', RefreshView.as_view(), name='refresh_token'),  # Changed the name to remove spaces
    path('protected/', ProtectedView.as_view(), name='protected'),
    path('user/me/', MeView.as_view(), name='get_user_info'),  # Changed the name to remove spaces
    path('change-password/', ChangePasswordView.as_view(), name='change_password'),  # Changed the name to remove spaces
    path('logout/', LogoutView.as_view(), name='logout'),

    path('forgot-password/', ForgotPasswordView.as_view(), name='forgot_password'),
    path('reset-password/', VerifyOTPView.as_view(), name='verify_otp'),
]
