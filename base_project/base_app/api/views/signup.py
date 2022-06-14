import logging
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from rest_framework.views import APIView
from django.contrib.auth import get_user_model
from django.urls import reverse

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

            group_data = request.user.groups.filter(name__exact='manager').exists()
            LOGGER.debug("group_data exist %s", group_data)
            a = self.User.objects.get(email=request.data["email"])
            for i in a:
                LOGGER.debug("i %s", i)
            if self.User.objects.get(email=request.data["email"]):
                old_data = self.User.objects.get(roll=request.data["roll"])

                LOGGER.debug("old_data %s", old_data)
            #     serializer = EmployeeInfoSerializer(
            #         old_data,
            #         data=request.data,
            #         partial=True
            #     )
            #     if serializer.is_valid(raise_exception=True):
            #         serializer.save()
            #         return Response(status=HTTP_201_CREATED, data=serializer.data)
            #
            # return Response(status=HTTP_400_BAD_REQUEST, data="wrong parameters")
