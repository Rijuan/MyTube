from django.contrib import admin

from .models import name_User, userProfile, Channel, Videos, Subscriber, Watch, Likes
# Register your models here.
admin.site.register(name_User)
admin.site.register(userProfile)
admin.site.register(Channel)
admin.site.register(Videos)
admin.site.register(Subscriber)
admin.site.register(Watch)
admin.site.register(Likes)
