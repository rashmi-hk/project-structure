import json
import logging
from ...models import EmployeeInfo
from ...serializer import EmployeeInfoSerializer
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.authentication import SessionAuthentication
from rest_framework.throttling import AnonRateThrottle , UserRateThrottle
from rest_framework.response import Response
from django.core import serializers
from rest_framework import status
from django.contrib.auth import get_user_model
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK,
    HTTP_201_CREATED,
)
LOGGER = logging.getLogger(__name__)

class EmployeeAPI(APIView):

    def __init__(self, **kwargs):
        super(EmployeeAPI, self).__init__(**kwargs)
        self.User = get_user_model()

    # If we uncomment this post class doesnot work
    # authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    throttle_class = [AnonRateThrottle, UserRateThrottle]

    def get(self, request):
        LOGGER.debug("Inside get employee info")
        emp_data = EmployeeInfo.objects.all()
        data = serializers.serialize('json', emp_data)
        return_status = status.HTTP_200_OK
        return Response(data=json.dumps(data), status=return_status)

    def post(self, request):
        LOGGER.debug("Inside post emp")
        user_dict = {}
        if 'name' in request.data:
            user_dict["name"] = request.data['name']
        if 'address' in request.data:
            user_dict["address"] = request.data['address']
        if 'roll' in request.data:
            user_dict["roll"] = request.data['roll']
        if 'department' in request.data:
            user_dict["department"] = request.data['department']
        if 'is_manager' in request.data:
            user_dict["is_manager"] = request.data['is_manager']

        LOGGER.debug("User dict %s", user_dict)
        user = EmployeeInfo.objects.create(**user_dict)
        return Response(data=user_dict,
                        status=HTTP_200_OK)

    def patch(self, request):
        """
        update employee records based on given request
        """
        LOGGER.debug("Inside patch method")
        LOGGER.debug("Request %s", request.data)
        if 'is_manager' and 'roll' in request.data:

            group_data = request.user.groups.filter(name__exact='manager').exists()
            LOGGER.debug("group_data exist %s", group_data)

            if EmployeeInfo.objects.get(roll=request.data["roll"]):
               old_data = EmployeeInfo.objects.get(roll=request.data["roll"])
               serializer = EmployeeInfoSerializer(
                   old_data,
                   data=request.data,
                   partial=True
               )
               if serializer.is_valid(raise_exception=True):
                  serializer.save()
                  return Response(status=HTTP_201_CREATED, data=serializer.data)

            return Response(status=HTTP_400_BAD_REQUEST, data="wrong parameters")



#
#
# INSERT INTO Employee_info (id,create_datetime,create_user,create_program,modify_datetime,modify_user,modify_program,name,department ,address,roll)
# VALUES(1,'12/06/2022','reashmi','emp','12/06/2022','rashmi','rashmi','parimala',	'dev', 'musore', 'developer');