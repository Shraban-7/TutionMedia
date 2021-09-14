from django.urls import path
from .views import login_user, logout_user, registration, change_password, activate, user_profile, ownerProfile, \
    updateprofile, Teacher_list, MemberShip,filter
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, \
    PasswordResetCompleteView

# app_name='accounts'

urlpatterns = [
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', registration, name='signup'),
    path('password/', change_password, name='change_password'),
    path('activate/<uidb64>/<token>/', activate, name='activate'),
    path('profile/', user_profile, name='profile'),
    path('ownerprofile/', ownerProfile, name='ownerprofile'),
    path('updateprofile/', updateprofile, name='updateprofile'),
    path('membership/', MemberShip.as_view(), name='membership'),
    # path('contact/', Contact.as_view(), name='contact'),
    path('search/', filter, name='search'),

    path('list/', Teacher_list.as_view(), name='list'),
    path('reset/password/', PasswordResetView.as_view(template_name='registrations/reset_password.html'),
         name='password_reset'),
    path('reset/password/done', PasswordResetDoneView.as_view(template_name='registrations/reset_password_done.html'),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>/',
         PasswordResetConfirmView.as_view(template_name='registrations/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('reset/done/', PasswordResetCompleteView.as_view(template_name='registrations/password_reset_complete.html'),
         name='password_reset_complete'),

]
