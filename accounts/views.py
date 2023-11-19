from rest_framework.generics import GenericAPIView
from rest_framework.views import APIView
from django.contrib.auth import get_user_model
from rest_framework.response import Response

User = get_user_model()


class RegisterAPIView(APIView):

    def post(self, request):
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        username = request.POST.get("username")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")

        if password == confirm_password:
            if User.objects.filter(email=email).exists():
                return Response({'success': False, 'message': 'This email already exists!'}, status=400)
            if User.objects.filter(username=username).exists():
                return Response({'success': False, 'message': 'This username already exists!'}, status=400)
            else:
                user = User.objects.create_user(
                    first_name=first_name,
                    last_name=last_name,
                    email=email,
                    username=username,
                    password=confirm_password,
                )
                return Response({'success': True, 'message': 'Successfully register!'}, status=200)
        else:
            return Response({'success': False, 'message': 'Passwords are not same!'})

