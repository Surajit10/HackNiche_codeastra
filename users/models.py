from django.db import models

# Create your models here.
# Create your models here.


# Create your models here.
class Register(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100, null=False)
    emailid = models.CharField(max_length=100, null=False)
    fname = models.CharField(max_length=100, null=False)
    lname = models.CharField(max_length=100, null=False)
    gender = models.CharField(max_length=100, null=False)
    country = models.CharField(max_length=100, null=False)
    city = models.CharField(max_length=100, null=False)
    mobileno = models.CharField(max_length=10, null=False)
    dob = models.CharField(max_length=100, null=False)
    password1 = models.CharField(max_length=100, null=False)
    collegename = models.CharField(max_length=100, null=False)

class Contact(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=34, null=True)
    email = models.CharField(max_length=20)
    message = models.TextField()
    timeStamp = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return 'Message from ' + self.name + ' -' + self.email


class RegisterHackathon(models.Model):
    name_hackathon = models.CharField(max_length=20, null=False)
    Organization_name = models.CharField(max_length=20, null=False)
    Description_hack = models.TextField(max_length=200, null=False)
    rules = models.TextField(max_length=200, null=False)
    hackathon_url = models.CharField(max_length=200, null=False)
    domain = models.CharField(max_length=100, default=0,null=False)
    skills = models.CharField(max_length=100, default=0,null=False)
    Guidelines = models.TextField(max_length=500, null=False)
    start_date_time = models.DateTimeField(max_length=100)
    end_date_time = models.DateTimeField(max_length=100)
    minimum_no_team = models.IntegerField(default=0)
    maximum_no_team = models.IntegerField(default=0)
    MY_CHOICES = (
        ('Online', '0'),
        ('Offline', '1'),
        
    )
    mode_of_event = models.CharField(max_length=10, choices=MY_CHOICES,default = 'Offline')



class ParticipateHackathon(models.Model):
    name = models.CharField(max_length=20, null=False,default=0)
    email = models.EmailField(max_length=200, null=False,default=0)
    gender = models.CharField(max_length=200, null=False,default=0)
    college_name = models.CharField(max_length=200, null=False,default=0)
    domain = models.CharField(max_length=200, null=False,default=0)
    course = models.CharField(max_length=500, null=False,default=0)
    c_spec = models.CharField(max_length=200, null=False,default=0)
    year = models.CharField(max_length=200, null=False,default=0)
    diff_able = models.CharField(max_length=200, null=False,default=0)
    citizen = models.CharField(max_length=200, null=False,default=0)
    github = models.CharField(max_length=200, null=False,default=0)
    resume =models.FileField(upload_to='documents/',default=0)
    skills = models.TextField(max_length=400, null=False,default=0)
    experience = models.TextField(max_length=400, null=False,default=0)
    designation = models.TextField(max_length=400, null=False,default=0)
    no_of_exp = models.TextField(max_length=400, null=False,default=0)
    no_of_repos = models.IntegerField(null=False,default=0)
    no_of_stars = models.IntegerField(null=False,default=0)
    score = models.IntegerField(null=False,default=0)
    languages_used = models.TextField(max_length=400, null=False,default=0)
    hack_id = models.CharField(max_length=100, null=False,default=0)
    teamname = models.CharField(max_length=100, null=False,default=0)
    # resune = models.FileField(upload_to='media/documents', null=True, blank=True)

class Teams(models.Model):
    id = models.AutoField(primary_key=True)
    teamname = models.CharField(max_length=20, null=False,default=0)
    hackid = models.CharField(max_length=20, null=False,default=0)