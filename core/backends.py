from django.contrib.auth.backends import BaseBackend
from .models import User


class UsernameAuthBackend(BaseBackend):
    """Custom authentication backend using u_name field."""
    
    def authenticate(self, request, u_name=None, password=None, **kwargs):
        try:
            user = User.objects.get(u_name=u_name)
            if user.check_password(password):
                return user
        except User.DoesNotExist:
            return None
    
    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
