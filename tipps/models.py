from django.db import models
from django.contrib.auth.models import User
from matches.models import Match, Team

class Profile(models.Model):
    user = models.OneToOneField(User)
    points = models.IntegerField(default=0)
    ranking = models.IntegerField(default=1)
    betting_with_money = models.BooleanField(default=False)
    tendency = models.IntegerField(default=0)
    champion = models.ForeignKey(Team)

class Tip(models.Model):
    match = models.ForeignKey(Match)
    profile = models.ForeignKey(Profile)
    home_score = models.IntegerField(default=-1)
    away_score = models.IntegerField(default=-1)
    winner = models.ForeignKey(Team)
    points = models.IntegerField(default=0)
