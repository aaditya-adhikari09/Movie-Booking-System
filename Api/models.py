from django.db import models
# Create your models here.
# from django.db import models
class User(models.Model):
    full_name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    full_address = models.CharField(max_length=400)
    role = models.CharField(max_length=400)
    bio = models.CharField(max_length=300)
    phone = models.CharField(max_length=30)

class Experience(models.Model):
    company_name = models.CharField(max_length=300)
    start_end = models.CharField(max_length=300)
    experience_role = models.CharField(max_length=300)  # Change the field name
    description = models.CharField(max_length=300)
    tech_stack = models.CharField(max_length=300)
    responsibilities = models.CharField(max_length=300)
    url = models.CharField(max_length=300)
    langauge = models.CharField(max_length=300)
    user = models.ForeignKey(User, on_delete=models.CASCADE,default=1)


    
    def __str__(self):
        return self.company_name + self.description


class Education(models.Model):
    college_name = models.CharField(max_length=300)
    university_name = models.CharField(max_length=300)
    degree_name = models.CharField(max_length=300)
   

class Projects(models.Model):
    title = models.CharField(max_length=300)
    start_end=models.CharField(max_length=300)
    description = models.CharField(max_length=300)
    techstack = models.CharField(max_length=300)
    responsibilities = models.CharField(max_length=300)
    live_url = models.CharField(max_length=300)
    github_url= models.CharField(max_length=300)

