# from django.contrib.auth.models import User
# from django.contrib.auth.hashers import check_password

# class YourCustomAuthBackend:
#     def authenticate(self, request, username=None, password=None):
#         try:
#             user = User.objects.get(username=username)
#             if user.check_password(password):
#                 user.backend = 'django.contrib.auth.backends.ModelBackend'
#                 return user
#         except User.DoesNotExist:
#             return None
