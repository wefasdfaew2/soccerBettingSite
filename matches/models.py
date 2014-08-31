from django.db import models

class Group(models.Model):
    name = models.CharField(max_length=50)

class Stage(models.Model):
    name = models.CharField(max_length=50)

class Team(models.Model):
    name = models.CharField(max_length=50)
    flag = models.CharField(max_length=50)
    group = models.ForeignKey(Group)
    group_position = models.IntegerField()
    group_matches_played = models.IntegerField(default=0)
    group_matches_won = models.IntegerField(default=0)
    group_matches_deuce = models.IntegerField(default=0)
    group_matches_lost = models.IntegerField(default=0)
    group_goals = models.IntegerField(default=0)
    group_goals_against = models.IntegerField(default=0)
    group_points = models.IntegerField(default=0)

class Match(models.Model):
    stage = models.ForeignKey(Stage)
    group = models.ForeignKey(Group)
    home_team = models.ForeignKey(Team, related_name='math_home_set')
    away_team = models.ForeignKey(Team, related_name='match_away_set')
    home_score = models.IntegerField(default=-1)
    away_score = models.IntegerField(default=-1)
    finished = models.BooleanField(default=False)
    winner = models.ForeignKey(Team, related_name='match_winner_set')
    date = models.DateTimeField()
    city = models.CharField(max_length=50)
