from django.shortcuts import render, redirect
from django.contrib import messages
from rest_framework.views import APIView
from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.mail import EmailMessage, send_mail
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth import authenticate, login, logout


class SignInAPI(APIView):

    def __init__(self, **kwargs):
        super(SignInAPI, self).__init__(**kwargs)
        self.User = get_user_model()

    def get(self, request):
        print("This is get signin")
        return render(request, 'signin.html')

    def post(self, request):
        print("Inside signin post")
        username = request.POST['username']
        pass1 = request.POST['pass1']

        user = authenticate(username=username, password=pass1)

        if user is not None:
            login(request, user)
            fname = user.first_name
            messages.success(request, "Logged In Sucessfully!!")
            return render(request, "index.html", {"fname": fname})
        else:
            messages.error(request, "Bad Credentials!!")
            return redirect('signin')

        return render(request, 'signin')


class SignOutAPI(APIView):

    def get(self, request):
        logout(request)
        messages.success(request, "Logged Out Successfully!!")
        return redirect('home')