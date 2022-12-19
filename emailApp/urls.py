from django.urls import path
from .views import *
from . import views

urlpatterns = [
    # path("signup/",views.signupUser_list),
    # path("signup/<int:id>",views.signupUser_detail),
    path("signup/",SignupClass.as_view()),
    path("login/",LoginView.as_view()), 
    path("testLogin/",TestCaseForLogin.as_view()),
    path("forgotPassword/",ForgotPassword.as_view()),
    path("newpassword/<int:id>",NewPassword.as_view()), 
    path("forgetpasswordforuser/<int:id>/<str:token>",ForgotPassword.as_view()), 
    # path("logout/",LogoutView.as_view()),
    # path("signupClass/<int:id>",SignupClass.as_view()),
]
