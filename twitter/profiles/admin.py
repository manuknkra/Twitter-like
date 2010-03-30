from django.contrib import admin
from twitter.profiles.models import *

admin.site.register(account)
admin.site.register(Tweet)
admin.site.register(Following)
admin.site.register(Follower)
