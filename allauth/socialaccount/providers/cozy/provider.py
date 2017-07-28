from allauth.socialaccount.providers.base import ProviderAccount
from allauth.socialaccount.providers.oauth2.provider import OAuth2Provider


class CozyAccount(ProviderAccount):


    def get_profile_urs(self):
        return 'http://cozy.nyc/user/' + self.account.extra_data.get('username')

    def to_str(self):
        dflt = super(CozyAccount,self).to_str()
        username = self.account.extra_data.get('username')
        return username



class CozyProvider(OAuth2Provider):
    id = 'cozy'
    name = 'Cozy'
    account_class = CozyAccount

    def extract_uid(self,data):
        return data['username']

    def extract_common_fields(self,data):
        return dict(username = data.get('username'),)



provider_classes = [CozyProvider]
