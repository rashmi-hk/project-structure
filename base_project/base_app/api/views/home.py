from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from rest_framework.views import APIView
from django.contrib.auth import get_user_model


class HomeAPI(APIView):

    def __init__(self, **kwargs):
        super(HomeAPI, self).__init__(**kwargs)
        self.User = get_user_model()

    def get(self, request):
        print("This is home get")
        return render(request, "index.html")

