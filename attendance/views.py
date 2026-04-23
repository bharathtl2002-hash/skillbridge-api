from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.contrib.auth.hashers import make_password, check_password
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from attendance.models import User, Batch, Attendance, Session
from attendance.serializers import BatchSerializer, AttendanceSerializer, SessionSerializer

def get_user_from_token(request):
    auth = JWTAuthentication()
    user_auth_tuple = auth.authenticate(request)
    if user_auth_tuple is None:
        return None
    validated_token = user_auth_tuple[1]
    user_id = validated_token.get('user_id')
    return User.objects.filter(id=user_id).first()
@api_view(['POST'])
def signup(request):
    data = request.data.copy()
    password = data.get('password')
    if not password:
        return Response({"error": "Password required"}, status=400)
    if User.objects.filter(email=data.get('email')).exists():
        return Response({"error": "Email already exists"}, status=400)
    data['password'] = make_password(password)
    user = User.objects.create(**data)
    token = RefreshToken.for_user(user)
    return Response({
        "message": "User created",
        "token": str(token.access_token)
    })

@api_view(['POST'])
def login(request):
    email = request.data.get('email')
    password = request.data.get('password')

    user = User.objects.filter(email=email).first()

    if not user:
        return Response({"error": "User not found"}, status=404)

    if not check_password(password, user.password):
        return Response({"error": "Invalid password"}, status=401)
    token = RefreshToken.for_user(user)
    token['role'] = user.role
    return Response({
        "token": str(token.access_token),
        "role": user.role
    })

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_batch(request):
    user = get_user_from_token(request)

    if not user or user.role != "trainer":
        return Response({"error": "Forbidden"}, status=403)

    serializer = BatchSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_session(request):
    user = get_user_from_token(request)
    if not user or user.role != "trainer":
        return Response({"error": "Forbidden"}, status=403)
    serializer = SessionSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def mark_attendance(request):
    user = get_user_from_token(request)

    if not user or user.role != "student":
        return Response({"error": "Forbidden"}, status=403)

    data = request.data
    data['student'] = user.id   

    serializer = AttendanceSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

    return Response(serializer.errors)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_attendance(request, session_id):
    user = get_user_from_token(request)

    if not user or user.role != "trainer":
        return Response({"error": "Forbidden"}, status=403)

    records = Attendance.objects.filter(session_id=session_id)
    serializer = AttendanceSerializer(records, many=True)

    return Response(serializer.data)