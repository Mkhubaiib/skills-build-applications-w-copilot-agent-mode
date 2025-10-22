from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard
from datetime import date, timedelta


class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        self.stdout.write('Populating database with sample data...')

        # Clear existing data
        Leaderboard.objects.all().delete()
        Activity.objects.all().delete()
        Workout.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()

        # Create Teams - Marvel and DC themed
        team_marvel = Team.objects.create(
            name='Team Marvel',
            description='Earth\'s Mightiest Heroes staying fit'
        )
        team_dc = Team.objects.create(
            name='Team DC',
            description='Justice League fitness enthusiasts'
        )

        # Create Users - Superhero themed
        users_data = [
            {'name': 'Iron Man', 'email': 'ironman@marvel.com', 'team': team_marvel, 'is_superhero': True},
            {'name': 'Captain America', 'email': 'cap@marvel.com', 'team': team_marvel, 'is_superhero': True},
            {'name': 'Black Widow', 'email': 'widow@marvel.com', 'team': team_marvel, 'is_superhero': True},
            {'name': 'Batman', 'email': 'batman@dc.com', 'team': team_dc, 'is_superhero': True},
            {'name': 'Superman', 'email': 'superman@dc.com', 'team': team_dc, 'is_superhero': True},
            {'name': 'Wonder Woman', 'email': 'wonderwoman@dc.com', 'team': team_dc, 'is_superhero': True},
        ]

        users = []
        for user_data in users_data:
            user = User.objects.create(**user_data)
            users.append(user)
            self.stdout.write(f'Created superhero user: {user.name}')

        # Create Activities - Superhero training themed
        activity_types = ['Flight Training', 'Strength Training', 'Combat Practice', 'Endurance Run', 'Agility Drills', 'Team Strategy']
        for i, user in enumerate(users):
            for j in range(5):
                Activity.objects.create(
                    user=user,
                    type=activity_types[j % len(activity_types)],
                    duration=45 + (i * 15) + (j * 10),
                    date=date.today() - timedelta(days=j)
                )
        self.stdout.write('Created superhero training activities for all users')

        # Create Workouts - Superhero themed
        workouts_data = [
            {
                'name': 'Avengers Assembly Workout',
                'description': 'High-intensity team training session for Earth\'s Mightiest Heroes'
            },
            {
                'name': 'Justice League Power Hour',
                'description': 'Strength and endurance training worthy of the Justice League'
            },
            {
                'name': 'Hero Conditioning',
                'description': 'All-around fitness program for maintaining superhero status'
            },
            {
                'name': 'Infinity Gauntlet Challenge',
                'description': 'Ultimate endurance test - can you handle the power?'
            },
        ]

        for workout_data in workouts_data:
            workout = Workout.objects.create(
                name=workout_data['name'],
                description=workout_data['description']
            )
            # Assign users to suggested_for
            workout.suggested_for.add(users[0], users[1], users[3])
            self.stdout.write(f'Created workout: {workout.name}')

        # Create Leaderboard entries
        Leaderboard.objects.create(
            team=team_marvel,
            points=550
        )
        self.stdout.write(f'Created leaderboard entry for {team_marvel.name}: 550 points')
        
        Leaderboard.objects.create(
            team=team_dc,
            points=480
        )
        self.stdout.write(f'Created leaderboard entry for {team_dc.name}: 480 points')

        self.stdout.write(self.style.SUCCESS('Successfully populated database with superhero sample data!'))
