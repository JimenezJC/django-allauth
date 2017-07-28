import requests
from allauth.socialaccount.providers.oauth2.views import(
    OAuth2Adapter,
    OAuth2CallbackView
    OAuth2LoginView,
)

from .providers CozyProvider


class CozyOAuth2Adapter(OAuth2Adapter):
    provider_id = CozyProvider.id
    access_tokens_url = '' #add later
    authorize_url = '' #add later
    profile_url ='' #add later

    def complete_login(self,request,app,token,**kwargs):
        resp = request.get(
            self.profile_url,
            params = {'oauth_token': token.token}
        )
        extra_data = resp.json()
        return self.get_provider().sociallogin_form_response(request,extra_data)


oauth2_login  = OAuth2LoginView.adapter_view(CozyOAuth2Adapter)
oauth2_callback = OAuth2CallbackView.adapter_view(CozyOAuth2Adapter)
