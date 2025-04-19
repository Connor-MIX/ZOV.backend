from rest_framework.response import Response
from django.shortcuts import redirect
from allauth.socialaccount.providers.github.views import GitHubOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from dj_rest_auth.registration.views import SocialLoginView
import os

class GitHubLogin(SocialLoginView):
    adapter_class = GitHubOAuth2Adapter
    client_class = OAuth2Client
    callback_url = 'http://localhost:8000/accounts/github/login/callback/'

    def get(self, request):
        code = request.query_params.get('code')
        
        if not code:
            # Перенаправляем на GitHub для авторизации
            client_id = os.getenv("GITHUB_CLIENT_ID")
            scope = 'user:email'
            auth_url = f"https://github.com/login/oauth/authorize?client_id={client_id}&redirect_uri={self.callback_url}&scope={scope}"
            return redirect(auth_url)

        self.request = request
        self.request.data = {'code': code}
        
        # Получаем токен
        self.serializer = self.get_serializer(data=self.request.data)
        self.serializer.is_valid(raise_exception=True)
        
        login = self.serializer.save()
        
        # Возвращаем токен доступа
        return Response({
            'access_token': login.token,
            'user': {
                'id': login.user.id,
                'email': login.user.email,
                'username': login.user.username
            }
        })