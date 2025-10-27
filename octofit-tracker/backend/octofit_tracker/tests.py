from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class ModelTests(TestCase):
    def test_team_creation(self):
        team = Team.objects.create(name='Marvel', description='Marvel Superheroes')
        self.assertEqual(team.name, 'Marvel')

    def test_user_creation(self):
        team = Team.objects.create(name='DC', description='DC Superheroes')
        user = User.objects.create(name='Superman', email='superman@dc.com', team=team)
        self.assertEqual(user.team.name, 'DC')

    def test_activity_creation(self):
        team = Team.objects.create(name='Marvel', description='Marvel Superheroes')
        user = User.objects.create(name='Iron Man', email='ironman@marvel.com', team=team)
        activity = Activity.objects.create(user=user, type='Running', duration=30, calories=300)
        self.assertEqual(activity.user.name, 'Iron Man')

    def test_workout_creation(self):
        workout = Workout.objects.create(name='Cardio', description='Cardio workout')
        self.assertEqual(workout.name, 'Cardio')

    def test_leaderboard_creation(self):
        team = Team.objects.create(name='Marvel', description='Marvel Superheroes')
        leaderboard = Leaderboard.objects.create(team=team, total_calories=1000, total_duration=120)
        self.assertEqual(leaderboard.team.name, 'Marvel')
