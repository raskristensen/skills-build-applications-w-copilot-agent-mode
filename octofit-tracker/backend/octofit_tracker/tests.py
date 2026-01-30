from django.test import TestCase
from .models import User, Team, Activity, Leaderboard, Workout

class ModelTests(TestCase):
    def test_team_creation(self):
        team = Team.objects.create(name='Test Team', description='A test team')
        self.assertEqual(str(team), 'Test Team')

    def test_user_creation(self):
        team = Team.objects.create(name='Test Team2', description='A test team2')
        user = User.objects.create(name='Test User', email='test@example.com', team=team, is_superhero=True)
        self.assertEqual(str(user), 'Test User')

    def test_workout_creation(self):
        workout = Workout.objects.create(name='Test Workout', description='desc', difficulty='Easy')
        self.assertEqual(str(workout), 'Test Workout')

    def test_leaderboard_creation(self):
        team = Team.objects.create(name='Test Team3', description='A test team3')
        leaderboard = Leaderboard.objects.create(team=team, total_points=100, rank=1)
        self.assertEqual(str(leaderboard), 'Test Team3 - 100 pts')

    def test_activity_creation(self):
        team = Team.objects.create(name='Test Team4', description='A test team4')
        user = User.objects.create(name='Test User2', email='test2@example.com', team=team, is_superhero=False)
        workout = Workout.objects.create(name='Test Workout2', description='desc2', difficulty='Medium')
        activity = Activity.objects.create(user=user, workout=workout, date='2026-01-30T10:00:00Z', duration_minutes=30, calories_burned=100)
        self.assertEqual(str(activity), 'Test User2 - Test Workout2 on 2026-01-30 10:00:00+00:00')
