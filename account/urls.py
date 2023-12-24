from django.urls import path,include
from django.contrib.auth import views as auth_views
from .import views

urlpatterns = [


    path('', views.dashboard, name='dashboard'),

    #Custom authentication view url.
    # path('login/', views.user_login, name='login'),


    # #**************Django`s default authentication views which we can use instead of writing our own Custom authentication view.**************
    
    #     ##Login and logout views deals with the authentication.

    #         #Handles a login form and logs in a user
    #         path('login/', auth_views.LoginView.as_view(), name='login'),
            
    #         #Logs out a user
    #         path('logout/', auth_views.LogoutView.as_view(), name='logout'),
        


    #     ##Change password views allows users to be able to change their password after they log into the site

    #         #Handles a form to change the user’s password
    #         path('password-change/', auth_views.PasswordChangeView.as_view(), name='password_change'),

    #         #The success view that the user is redirected to after a successful password change
    #         path('password-change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),



    #     ##Reset password views Allows users to reset their password in case they forgot their password.. 

    #         # It generates a one-time-use link with a token and sends it to a user’s email account
    #         path('password-reset/',
    #             auth_views.PasswordResetView.as_view(),
    #             name='password_reset'),

    #         #Tells users that an email—including a link to reset their password—has been sent to them
    #         path('password-reset/done/',
    #             auth_views.PasswordResetDoneView.as_view(),
    #             name='password_reset_done'),
            
    #         #Allows users to set a new password
    #         path('password-reset/<uidb64>/<token>/',
    #             auth_views.PasswordResetConfirmView.as_view(),
    #             name='password_reset_confirm'),
            
    #         #The success view that the user is redirected to after successfully resetting their password
    #         path('password-reset/complete/',
    #             auth_views.PasswordResetCompleteView.as_view(),
    #             name='password_reset_complete'),


        #Django provides URL patterns for the authentication views that are equivalent to the ones we just created. 
        # We will replace the authentication URL patterns with the ones provided by Django.
        path('', include('django.contrib.auth.urls')),
        path('register/', views.register, name='register'),
        path('edit/', views.edit, name='edit'),
]
