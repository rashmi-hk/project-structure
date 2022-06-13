import json

from ...models import EmployeeInfo
from ...serializer import EmployeeInfoSerializer
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.authentication import SessionAuthentication
from rest_framework.throttling import AnonRateThrottle , UserRateThrottle
from rest_framework.response import Response
from django.core import serializers
from rest_framework import status
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)

class EmployeeAPI(APIView):

    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    throttle_class = [AnonRateThrottle, UserRateThrottle]

    def get(self, request):
        print("Inside get employee info")
        emp_data = EmployeeInfo.objects.all()
        data = serializers.serialize('json', emp_data)
        return_status = status.HTTP_200_OK
        return Response(data=json.dumps(data), status=return_status)

    def post(self, request):
        print("Inside post emp")
        user_dict = {}
        if 'name' in request.data:
            user_dict["name"] = request.data['name']
        if 'address' in request.data:
            user_dict["address"] = request.data['address']
        if 'roll' in request.data:
            user_dict["roll"] = request.data['roll']
        if 'department' in request.data:
            user_dict["department"] = request.data['department']

        print("User dict %s", user_dict)
        user = EmployeeInfo.objects.create(**user_dict)
        return Response(data=user_dict,
                        status=HTTP_200_OK)


#
#
# INSERT INTO Employee_info (id,create_datetime,create_user,create_program,modify_datetime,modify_user,modify_program,name,department ,address,roll)
# VALUES(1,'12/06/2022','reashmi','emp','12/06/2022','rashmi','rashmi','parimala',	'dev', 'musore', 'developer');