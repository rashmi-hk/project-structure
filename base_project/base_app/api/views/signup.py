from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from rest_framework.views import APIView
from django.contrib.auth import get_user_model


class SignUpAPI(APIView):

    def __init__(self, **kwargs):
        super(SignUpAPI, self).__init__(**kwargs)
        self.User = get_user_model()

    def get(self, request):
        print("This is get")
        return render(request, "signup.html")

    def post(self, request):
        print("Inside post")
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        if self.User.objects.filter(username=username):
            print("Username already exist! Please try some other username")
            messages.error(request, "Username already exist! Please try some other username.")
            return redirect('home/')

        if self.User.objects.filter(email=email).exists():
            print("Email Already Registered!!")
            messages.error(request, "Email Already Registered!!")
            return redirect('home/')

        if len(username) > 20:
            print("Username must be under 20 charcters!!")
            messages.error(request, "Username must be under 20 charcters!!")
            return redirect('home/')

        if pass1 != pass2:
            print("Passwords didn't matched!!")
            messages.error(request, "Passwords didn't matched!!")
            return redirect('home/')

        if not username.isalnum():
            print("Username must be Alpha-Numeric!!")
            messages.error(request, "Username must be Alpha-Numeric!!")
            return redirect('home/')

        myuser = self.User.objects.create_user(username, email, pass1)
        print("myuser %s", myuser)
        myuser.first_name = fname
        myuser.last_name = lname
        # myuser.is_active = False
        myuser.is_active = False
        myuser.save()
        print("Data saved")
        return render(request, "signin.html")
