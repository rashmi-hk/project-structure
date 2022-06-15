import json
import logging
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from rest_framework.views import APIView
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK,
    HTTP_201_CREATED,
)
from django.core import serializers
from rest_framework.response import Response
from django.forms.models import model_to_dict

LOGGER = logging.getLogger(__name__)

class SignUpAPI(APIView):

    def __init__(self, **kwargs):
        super(SignUpAPI, self).__init__(**kwargs)
        self.User = get_user_model()

    def get(self, request):
        LOGGER.debug("This is get")
        return render(request, "signup.html")

    def post(self, request):
        LOGGER.debug("Inside post")
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        if self.User.objects.filter(username=username):
            LOGGER.debug("Username already exist! Please try some other username")
            messages.error(request, "Username already exist! Please try some other username.")
            return redirect(reverse('signup'))

        if self.User.objects.filter(email=email).exists():
            LOGGER.debug("Email Already Registered!!")
            messages.error(request, "Email Already Registered!!")
            return redirect(reverse('signup'))

        if len(username) > 20:
            LOGGER.debug("Username must be under 20 charcters!!")
            messages.error(request, "Username must be under 20 charcters!!")
            return redirect(reverse('signup'))

        if pass1 != pass2:
            LOGGER.debug("Passwords didn't matched!!")
            messages.error(request, "Passwords didn't matched!!")
            return redirect(reverse('signup'))

        if not username.isalnum():
            LOGGER.debug("Username must be Alpha-Numeric!!")
            messages.error(request, "Username must be Alpha-Numeric!!")
            return redirect(reverse('signup'))

        myuser = self.User.objects.create_user(username, email, pass1)

        LOGGER.debug("myuser %s", myuser)
        myuser.first_name = fname
        myuser.last_name = lname
        # myuser.is_active = False
        myuser.is_active = True
        myuser.save()
        LOGGER.debug("Data saved")
        return render(request, 'signin.html')


    def patch(self, request):
        """
        update employee records based on given request
        """
        LOGGER.debug("Inside patch method")
        LOGGER.debug("Request %s", request.data)
        if 'email' in request.data:
            return_dict = {}

            group_data = request.user.groups.filter(name__exact='manager').exists()
            LOGGER.debug("group_data exist %s", group_data)
            user = self.User.objects.get(email=request.data["email"])

            if self.User.objects.get(email=request.data["email"]):
                old_data = self.User.objects.get(email=request.data["email"])
                LOGGER.debug("old_data %s", old_data)
            if user.groups.filter(name="manager"):
                LOGGER.debug("group data %s",user.groups.filter(name="manager"))
                self.User.objects.filter(email=request.data["email"]).update(is_staff = True)

                LOGGER.debug("Updated as True")
            else:
                return_dict.update({"is_active": False})
                self.User.objects.filter(email=request.data["email"]).update(is_staff=False)
                LOGGER.debug("Updated as false")

            user = self.User.objects.get(email=request.data["email"])


            return Response(status=HTTP_201_CREATED)

        return Response(status=HTTP_400_BAD_REQUEST, data="wrong parameters")


