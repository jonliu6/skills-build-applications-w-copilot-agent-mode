from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Clear existing data
        Activity.objects.all().delete()
        Workout.objects.all().delete()
        Leaderboard.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()

        # Create teams
        marvel = Team.objects.create(name='Marvel', description='Marvel Superheroes')
        dc = Team.objects.create(name='DC', description='DC Superheroes')

        # Create users
        users = [
            User(name='Iron Man', email='ironman@marvel.com', team=marvel),
            User(name='Captain America', email='cap@marvel.com', team=marvel),
            User(name='Thor', email='thor@marvel.com', team=marvel),
            User(name='Superman', email='superman@dc.com', team=dc),
            User(name='Batman', email='batman@dc.com', team=dc),
            User(name='Wonder Woman', email='wonderwoman@dc.com', team=dc),
        ]
        for user in users:
            user.save()

        # Create activities
        Activity.objects.create(user=users[0], type='Running', duration=30, calories=300)
        Activity.objects.create(user=users[1], type='Cycling', duration=45, calories=400)
        Activity.objects.create(user=users[3], type='Swimming', duration=60, calories=500)

        # Create workouts
        workout1 = Workout.objects.create(name='Cardio Blast', description='High intensity cardio workout')
        workout2 = Workout.objects.create(name='Strength Training', description='Build muscle strength')
        workout1.suggested_for.set([users[0], users[1], users[3]])
        workout2.suggested_for.set([users[2], users[4], users[5]])

        # Create leaderboards
        Leaderboard.objects.create(team=marvel, total_calories=700, total_duration=75)
        Leaderboard.objects.create(team=dc, total_calories=500, total_duration=60)

        self.stdout.write(self.style.SUCCESS('Test data populated successfully!'))
