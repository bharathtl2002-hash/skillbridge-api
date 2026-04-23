from django.db import models
class User(models.Model):
    ROLE_CHOICES = [
        ('student','student'),
        ('trainer','trainer'),
        ('institution','institution'),
        ('programme_manager','programme_manager'),
        ('monitoring_officer','monitoring_officer'),
    ]
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=200)
    role = models.CharField(max_length=30, choices=ROLE_CHOICES)
class Batch(models.Model):
    name = models.CharField(max_length=100)
class Session(models.Model):
    title = models.CharField(max_length=100)
    batch = models.ForeignKey(Batch, on_delete=models.CASCADE)
class Attendance(models.Model):
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=20)
    def __str__(self):
        return self.name