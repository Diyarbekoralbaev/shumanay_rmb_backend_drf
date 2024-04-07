from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import UserModel, OTPModel
from .serializers import SignupSerializer, LoginSerializer, ChangePasswordSerializer, ForgotPasswordSerializer, \
    ConfirmForgotPasswordSerializer
from django.contrib.auth.hashers import make_password, check_password
from rest_framework_simplejwt.tokens import AccessToken, RefreshToken
from drf_yasg.utils import swagger_auto_schema

from .utils import send_otp, generate_otp


@swagger_auto_schema(
    tags=['auth'],
    url='/auth/',  # Set the prefix here
)
class SignupView(APIView):
    @swagger_auto_schema(
        request_body=SignupSerializer,
        tags=['auth']
    )
    def post(self, request):
        serializer = SignupSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save(password=make_password(serializer.validated_data['password']))
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    @swagger_auto_schema(
        request_body=LoginSerializer,
        tags=['auth']
    )
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            user = UserModel.objects.filter(username=username).first()
            if user and check_password(password, user.password) and user.is_active:
                access_token = AccessToken.for_user(user)
                refresh_token = RefreshToken.for_user(user)
                return Response({'access_token': str(access_token), 'refresh_token': str(refresh_token)})
            raise AuthenticationFailed('Invalid username or password')
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RefreshView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    @swagger_auto_schema(
        tags=['auth'],
        security=[{'Bearer': []}],
    )
    def post(self, request):
        refresh_token = request.data.get('refresh_token')
        if not refresh_token:
            raise AuthenticationFailed('No refresh token provided')
        try:
            refresh = RefreshToken(refresh_token)
            access_token = refresh.access_token
            return Response({'access_token': str(access_token)})
        except Exception as e:
            raise AuthenticationFailed('Invalid refresh token')


class ProtectedView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    @swagger_auto_schema(
        tags=['auth'],
        security=[{'Bearer': []}],
    )
    def get(self, request):
        user = request.user
        return Response({'message': f'Hello {user.username}'})


class MeView(APIView):
    permission_classes = [IsAuthenticated,]
    authentication_classes = [JWTAuthentication,]

    @swagger_auto_schema(
        tags=['auth'],
        security=[{'Bearer': ['read', 'write    ']}],
        operation_id='me',
    )
    def get(self, request):
        user = request.user
        serializer = SignupSerializer(user)
        return Response(serializer.data)


class ChangePasswordView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    @swagger_auto_schema(
        request_body=ChangePasswordSerializer,
        tags=['auth'],
        security=[{'Bearer': []}],
    )
    def post(self, request):
        serializer = ChangePasswordSerializer(data=request.data)
        if serializer.is_valid():
            user = request.user
            old_password = serializer.validated_data['old_password']
            new_password = serializer.validated_data['new_password']
            if check_password(old_password, user.password):
                user.set_password(new_password)
                user.save()
                return Response({'message': 'Password changed successfully'})
            raise AuthenticationFailed('Old password is incorrect')
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LogoutView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    @swagger_auto_schema(
        tags=['auth'],
        security=[{'Bearer': []}],
    )
    def post(self, request):
        try:
            refresh_token = request.data['refresh_token']
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({'message': 'User logged out successfully'})
        except Exception as e:
            return Response({'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)


class ForgotPasswordView(APIView):
    @swagger_auto_schema(
        request_body=ForgotPasswordSerializer,
        tags=['auth']
    )
    def post(self, request):
        serializer = ForgotPasswordSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            user = UserModel.objects.filter(email=email).first()
            if user:
                otp_code = generate_otp()
                print(send_otp(email=email, otp=otp_code))
                print(otp_code)
                OTPModel.objects.create(user=user, otp=otp_code)
                return Response({'message': 'OTP sent successfully'})
            raise AuthenticationFailed('Email does not exist')
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class VerifyOTPView(APIView):
    @swagger_auto_schema(
        request_body=ConfirmForgotPasswordSerializer,
        tags=['auth']
    )
    def post(self, request):
        serializer = ConfirmForgotPasswordSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            otp_code = serializer.validated_data['otp_code']
            new_password = serializer.validated_data['new_password']
            user = UserModel.objects.filter(email=email).first()
            if user:
                otp = OTPModel.objects.filter(user=user, otp=otp_code).first()
                if otp and not otp.is_expired():
                    user.set_password(new_password)
                    user.save()
                    otp.delete()
                    return Response({'message': 'Password changed successfully'})
                raise AuthenticationFailed('Invalid OTP')
            raise AuthenticationFailed('Email does not exist')
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

