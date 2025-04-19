from django.shortcuts import redirect
from allauth.socialaccount.providers.github.views import GitHubOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from dj_rest_auth.registration.views import SocialLoginView
import os

class GitHubLogin(SocialLoginView):
    adapter_class = GitHubOAuth2Adapter
    client_class = OAuth2Client

    def get(self, request, *args, **kwargs):
        code = request.query_params.get('code')
        
        if not code:
            # Перенаправляем на GitHub для авторизации
            client_id = os.getenv("GITHUB_CLIENT_ID")
            redirect_uri = 'http://localhost:8000/accounts/github/login/callback/'
            auth_url = f"https://github.com/login/oauth/authorize?client_id={client_id}&redirect_uri={redirect_uri}"
            return redirect(auth_url)
        # Если code есть, обрабатываем его
        return super().get(request, *args, **kwargs)