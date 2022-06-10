from django.conf import settings
import re

from django.contrib.auth import get_user_model
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden

from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError, AuthenticationFailed




class LoginRequiredMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response
        print("One time Initialization")

    def __call__(self, request):
        print("This is before view")

        User = get_user_model()

        if re.search('/custom/', request.path):
            print("This is user api")
            return self.get_response(request)
        elif request.path != '/api/token/':
            try:
                print("Check athentication")
                jwt_obj = JWTAuthentication()
                header_obj = jwt_obj.get_header(request)
                if header_obj:
                    print("Token present in header")
                    raw_token = jwt_obj.get_raw_token(header_obj)
                    print("raw_token %s", raw_token)
                    validated_token = jwt_obj.get_validated_token(raw_token)
                    print("validated_token %s", validated_token)
                    request_user = jwt_obj.get_user(validated_token)
                    print("request_user %s", request_user)
                else:
                    return HttpResponseBadRequest("Token not provided in header.")
            except InvalidToken:
                return HttpResponseBadRequest("InvalidToken")
            except TokenError:
                return HttpResponseBadRequest("TokenError")
            except AuthenticationFailed:
                return HttpResponseBadRequest("AuthenticationFailed")
                # check given user authorized to use this service
                # check given user authorized to use this service
            print("check user")
            if User.objects.filter(username=request_user).exists():
                print("The user is authorized to use the system")
                # the user is authorized to use the system.
                return self.get_response(request)
            else:
                return HttpResponseForbidden("User is not authorized to use this service.")
        else:
            response = self.get_response(request)
            print("This is auth api")
            return response

