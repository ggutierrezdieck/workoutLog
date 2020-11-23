from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User

# Create your models here.


# class user(models.Model):
#     GENDER = (
#             ('M', 'MALE'),
#             ('F', 'FEMALE'),
#         )

#     email = models.EmailField()
#     dob = models.DateField()
#     gender = models.CharField(max_length=10, choices=GENDER)


class workout(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name='workouts')
    workoutDate = models.DateField()


class exercise(models.Model):
    workout = models.ForeignKey(workout, on_delete=models.CASCADE,
                                related_name='execises')
    excerciseName = models.CharField(max_length=250)
    sets = models.IntegerField(blank=True)
    reps = models.IntegerField(blank=True)
    effort = models.IntegerField(validators=[MinValueValidator(1),
                                 MaxValueValidator(5)])


class personalRecord(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name='usersPRs')
    excercise = models.ForeignKey(workout, on_delete=models.CASCADE,
                                  related_name='PR')
    excerciseName = models.CharField(max_length=250)
    weightReps = models.CharField(max_length=10)
