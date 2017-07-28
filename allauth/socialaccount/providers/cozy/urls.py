from allauth.socialaccount.providers.oauth2.urls import default_urlpatterns

from .provider import CozyProvider



urlpatterns = default_urlpatterns(CozyProvider)
