"""m4jam URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView as app_views
from tickets import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', auth_views.LoginView.as_view(template_name="registration/login.html"), name='login'),
    url(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'),
    url(r'^signup/$', app_views.as_view(template_name="signup.html"), name='signup'),
    url(r'^password_reset/$', auth_views.PasswordResetView.as_view(template_name="registration/password_reset_form.html"), name="password_reset"),
    url(r'^password_reset_confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', auth_views.PasswordResetConfirmView.as_view(template_name="registration/password_reset_confirm.html"), name="password_reset_confirm"),
    url(r'^password_reset_done/$', auth_views.PasswordResetDoneView.as_view(template_name="registration/password_reset_done.html"), name="password_reset_done"),
    url(r'^password_reset_complete/$',auth_views.PasswordResetCompleteView.as_view(template_name="registration/password_reset_complete.html"), name="password_reset_complete"),
    url(r'^dashboard/$', app_views.as_view(template_name="dashboard.html"), name='dashboard'),
    url(r'^new_ticket/$', views.new_ticket, name="new_ticket"),
    url(r'^ticket_list/$', views.ticket_list, name="ticket_list")

]
