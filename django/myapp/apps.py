# import os
# from django.apps import AppConfig
# 
# class MyAppConfig(AppConfig):
#     name = 'myapp'
#     verbose_name = "My Application"
#     def ready(self):
#         from django.contrib.auth.models import User
#         
#         username = os.environ.get("DJANGO_SUPERUSER_USERNAME")
#         password = os.environ.get("DJANGO_SUPERUSER_PASSWORD")
#         email = os.environ.get("DJANGO_SUPERUSER_EMAIL")
#         if not User.objects.filter(username=username).exists():
#             User.objects.create_superuser(username,
#                                           email,
#                                           password)
