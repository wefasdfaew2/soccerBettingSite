from django.contrib import admin

from tipps.models import Profile, Tip

for model in (Profile, Tip):
    admin.site.register(model)
