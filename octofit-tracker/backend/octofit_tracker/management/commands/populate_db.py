from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard
from datetime import date, timedelta


class Command(BaseCommand):
    help = 'Populate the database with sample data for OctoFit Tracker'

    def handle(self, *args, **options):
        self.stdout.write('Populating database with sample data...')

        # Clear existing data
        Leaderboard.objects.all().delete()
        Activity.objects.all().delete()
        Workout.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()

        # Create Teams
        team1 = Team.objects.create(
            name='Code Warriors',
            description='A team of dedicated developers'
        )
        team2 = Team.objects.create(
            name='Fitness Fanatics',
            description='Health enthusiasts who love to code'
        )
        team3 = Team.objects.create(
            name='Octocat Squad',
            description='GitHub lovers staying fit'
        )

        # Create Users
        users_data = [
            {'name': 'Alice Smith', 'email': 'alice@example.com', 'team': team1, 'is_superhero': True},
            {'name': 'Bob Johnson', 'email': 'bob@example.com', 'team': team1, 'is_superhero': False},
            {'name': 'Carol White', 'email': 'carol@example.com', 'team': team2, 'is_superhero': False},
            {'name': 'David Brown', 'email': 'david@example.com', 'team': team2, 'is_superhero': True},
            {'name': 'Eve Davis', 'email': 'eve@example.com', 'team': team3, 'is_superhero': False},
            {'name': 'Frank Miller', 'email': 'frank@example.com', 'team': team3, 'is_superhero': False},
        ]

        users = []
        for user_data in users_data:
            user = User.objects.create(**user_data)
            users.append(user)
            self.stdout.write(f'Created user: {user.name}')

        # Create Activities
        activity_types = ['Running', 'Cycling', 'Swimming', 'Yoga', 'Weight Training', 'Walking']
        for i, user in enumerate(users):
            for j in range(5):
                Activity.objects.create(
                    user=user,
                    type=activity_types[j % len(activity_types)],
                    duration=30 + (i * 10) + (j * 5),
                    date=date.today() - timedelta(days=j)
                )
        self.stdout.write('Created activities for all users')

        # Create Workouts
        workouts_data = [
            {
                'name': 'Morning Cardio Blast',
                'description': '30-minute high-intensity cardio workout to start your day'
            },
            {
                'name': 'Strength Builder',
                'description': 'Full-body strength training routine for all fitness levels'
            },
            {
                'name': 'Flexibility Flow',
                'description': 'Yoga and stretching session for improved flexibility'
            },
            {
                'name': 'Endurance Challenge',
                'description': 'Long-distance running or cycling workout'
            },
        ]

        for workout_data in workouts_data:
            workout = Workout.objects.create(
                name=workout_data['name'],
                description=workout_data['description']
            )
            # Assign random users to suggested_for
            workout.suggested_for.add(users[0], users[2], users[4])
            self.stdout.write(f'Created workout: {workout.name}')

        # Create Leaderboard entries
        teams = [team1, team2, team3]
        points = [450, 380, 320]
        for team, point in zip(teams, points):
            Leaderboard.objects.create(
                team=team,
                points=point
            )
            self.stdout.write(f'Created leaderboard entry for {team.name}: {point} points')

        self.stdout.write(self.style.SUCCESS('Successfully populated database with sample data!'))
