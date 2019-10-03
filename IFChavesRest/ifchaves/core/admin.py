from django.contrib import admin

from .models import Admin, Key, User, Lending

admin.site.register(Admin)
admin.site.register(Key)
admin.site.register(User)
admin.site.register(Lending)
