from django.contrib import admin

from matches.models import Group, Stage, Team, Match

for model in (Group, Stage, Team, Match):
    admin.site.register(model)
