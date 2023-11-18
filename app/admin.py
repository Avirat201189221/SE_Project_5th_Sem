from django.contrib import admin
from app.models import UserSubmission,UserAssignment,UserTest,Test
from django.contrib.auth.models import User
# Register your models here.
admin.site.register(UserSubmission)
admin.site.register(UserAssignment)
admin.site.register(UserTest)
admin.site.register(Test)