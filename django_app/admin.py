from django.contrib import admin
from .models import User, Course, Foursome

# Register your models here.
admin.site.register(User)
admin.site.register(Course)
admin.site.register(Foursome)