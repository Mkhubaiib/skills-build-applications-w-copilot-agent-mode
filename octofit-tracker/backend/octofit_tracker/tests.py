from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class ModelTests(TestCase):
    def test_create_team(self):
        team = Team.objects.create(name='Marvel', description='Marvel Superheroes')
        self.assertEqual(team.name, 'Marvel')

    def test_create_user(self):
        team = Team.objects.create(name='DC', description='DC Superheroes')
        user = User.objects.create(name='Superman', email='superman@dc.com', team=team, is_superhero=True)
        self.assertEqual(user.team.name, 'DC')

    def test_create_activity(self):
        team = Team.objects.create(name='Marvel', description='Marvel Superheroes')
        user = User.objects.create(name='Iron Man', email='ironman@marvel.com', team=team, is_superhero=True)
        activity = Activity.objects.create(user=user, type='Running', duration=30, date='2025-10-17')
        self.assertEqual(activity.type, 'Running')

    def test_create_workout(self):
        workout = Workout.objects.create(name='Cardio', description='Cardio workout')
        self.assertEqual(workout.name, 'Cardio')

    def test_create_leaderboard(self):
        team = Team.objects.create(name='Marvel', description='Marvel Superheroes')
        leaderboard = Leaderboard.objects.create(team=team, points=100)
        self.assertEqual(leaderboard.points, 100)
