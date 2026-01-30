from djongo import models

class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    class Meta:
        db_table = 'teams'
    def __str__(self):
        return self.name

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True, related_name='members')
    is_superhero = models.BooleanField(default=False)
    class Meta:
        db_table = 'users'
    def __str__(self):
        return self.name

class Workout(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    difficulty = models.CharField(max_length=50)
    class Meta:
        db_table = 'workouts'
    def __str__(self):
        return self.name

class Activity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='activities')
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE, related_name='activities')
    date = models.DateTimeField()
    duration_minutes = models.PositiveIntegerField()
    calories_burned = models.PositiveIntegerField()
    class Meta:
        db_table = 'activities'
    def __str__(self):
        return f"{self.user} - {self.workout} on {self.date}"

class Leaderboard(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='leaderboards')
    total_points = models.PositiveIntegerField(default=0)
    rank = models.PositiveIntegerField(default=0)
    class Meta:
        db_table = 'leaderboard'
    def __str__(self):
        return f"{self.team} - {self.total_points} pts"
