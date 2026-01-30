from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from django.utils import timezone

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        self.stdout.write(self.style.WARNING('Deleting old data...'))
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()
        Workout.objects.all().delete()

        self.stdout.write(self.style.SUCCESS('Creating teams...'))
        marvel = Team.objects.create(name='Marvel', description='Marvel superheroes')
        dc = Team.objects.create(name='DC', description='DC superheroes')

        self.stdout.write(self.style.SUCCESS('Creating users...'))
        users = [
            User(name='Spider-Man', email='spiderman@marvel.com', team=marvel, is_superhero=True),
            User(name='Iron Man', email='ironman@marvel.com', team=marvel, is_superhero=True),
            User(name='Wonder Woman', email='wonderwoman@dc.com', team=dc, is_superhero=True),
            User(name='Batman', email='batman@dc.com', team=dc, is_superhero=True),
        ]
        User.objects.bulk_create(users)

        self.stdout.write(self.style.SUCCESS('Creating workouts...'))
        workouts = [
            Workout(name='Push Ups', description='Upper body workout', difficulty='Easy'),
            Workout(name='Running', description='Cardio workout', difficulty='Medium'),
            Workout(name='Deadlift', description='Strength workout', difficulty='Hard'),
        ]
        Workout.objects.bulk_create(workouts)

        self.stdout.write(self.style.SUCCESS('Creating activities...'))
        users = list(User.objects.all())
        workouts = list(Workout.objects.all())
        activities = [
            Activity(user=users[0], workout=workouts[0], date=timezone.now(), duration_minutes=30, calories_burned=200),
            Activity(user=users[1], workout=workouts[1], date=timezone.now(), duration_minutes=45, calories_burned=400),
            Activity(user=users[2], workout=workouts[2], date=timezone.now(), duration_minutes=60, calories_burned=600),
            Activity(user=users[3], workout=workouts[1], date=timezone.now(), duration_minutes=50, calories_burned=350),
        ]
        Activity.objects.bulk_create(activities)

        self.stdout.write(self.style.SUCCESS('Creating leaderboard...'))
        Leaderboard.objects.create(team=marvel, total_points=600, rank=1)
        Leaderboard.objects.create(team=dc, total_points=950, rank=2)

        self.stdout.write(self.style.SUCCESS('Database populated with test data!'))
