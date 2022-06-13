from django.urls import path, include
from .api. views.user import UserAPI
from .api. views.employee import EmployeeAPI
from .api. views.home import HomeAPI
from .api. views.signup import SignUpAPI
from .api. views.signin import SignInAPI, SignOutAPI

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('signup/', SignUpAPI.as_view(), name='signup'),
    path('user/', UserAPI.as_view(), name='user'),
    path('employee/', EmployeeAPI.as_view(), name='emp'),
    path('home/', HomeAPI.as_view(), name='home'),

    path('signin/', SignInAPI.as_view(), name='signin'),
    path('signout/', SignOutAPI.as_view(), name='signout'),
    path('api-auth/', include('rest_framework.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]