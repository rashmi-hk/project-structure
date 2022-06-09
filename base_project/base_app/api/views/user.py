import getpass
import logging

from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist
from django.utils import timezone
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
# from sesame import utils
# from .utils.api_utils import get_yml_file
# from .utils.db_utils import DBUtils
from  ...serializer import UserInfoSerializer
from  ...models import UserInfo
from django.contrib.auth import authenticate
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from django.core import serializers
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
from rest_framework.response import Response

LOGGER = logging.getLogger(__name__)


class UserAPI(APIView):
    """
    apis performs as per given request
    """

    def __init__(self, **kwargs):
        super(UserAPI, self).__init__(**kwargs)
        self.User = get_user_model()
        # self.db_utils_obj = DBUtils()


    def post(self, request):
            """
            Create records for user as given request
            """

            LOGGER.debug("Inside User Post api method")
            LOGGER.debug("Request Data are: %s", request.data)
            return_dict = dict()
            user_dict = {}
            username = request.data.get("username")
            LOGGER.debug("username %s", username)

            password = request.data.get("password")
            LOGGER.debug("password %s", password)
            if username is None or password is None:
                return Response({'error': 'Please provide both username and password'},
                                status=HTTP_400_BAD_REQUEST)
            user = authenticate(username=username, password=password)
            if not user:
                return Response({'error': 'Invalid Credentials'},
                                status=HTTP_404_NOT_FOUND)

            if 'profile_pic_url' in request.data:
                user_dict["image_url"] = request.data['profile_pic_url']

            if 'phone_number' in request.data:
                user_dict["phone_number"] = request.data['phone_number']

            if self.User.objects.filter(email=request.data['email_id']).exists():
                a = self.User.objects.filter(email=request.data['email_id'])
                LOGGER.debug("&&&&&&&&&&& %", a)
                user_detail = self.User.objects.get(email=request.data['email_id']).id

                print("********* %s", user_detail)
                print("********* %s", user_detail)
                user_id = user_detail

            user_dict["user_id_id"] = user_id

            user = UserInfo.objects.create(**user_dict)
            # data = serializers.serialize('json', user_dict)
            # return HttpResponse({'user': user_dict}, content_type="application/json")
            # token, _ = Token.objects.get_or_create(user=user)
            return Response(data = user_dict,
                            status=HTTP_200_OK)
