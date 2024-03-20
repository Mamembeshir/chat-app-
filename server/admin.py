from django.contrib import admin
from .models import Channels,Category,Servers


# Register your models here.
admin.site.register(Channels)
admin.site.register(Category)
admin.site.register(Servers)

