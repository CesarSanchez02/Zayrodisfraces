from django.contrib import admin
from django.urls import path, include
from allauth.account.views import SignupView
from accounts.forms import CustomSignupForm

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/signup/', SignupView.as_view(form_class=CustomSignupForm), name='account_signup'),
    path('accounts/', include('allauth.urls')),
    path('', include('pages.urls')),
]
