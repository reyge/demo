from django.db import models

# Create your models here.


class Myinfo(models.Model):
    picture = models.BinaryField(null=True)
    name = models.CharField(max_length=20)
    post = models. CharField(max_length=20)
    fb = models. CharField(max_length=1028)
    instagram = models. CharField(max_length=1028)
    linkedin = models. CharField(max_length=1028)
    dob = models. CharField(max_length=20)
    phone = models. CharField(max_length=20)
    email = models. CharField(max_length=20, null=True)
    location = models. CharField(max_length=20)
    content = models.TextField()

    def __str__(self):
        return self.name


class Language(models.Model):
    title = models.CharField(max_length=20)
    rate = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Interest(models.Model):
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Education(models.Model):
    start_date = models.CharField(max_length=20)
    finish_date = models.CharField(max_length=20)
    degree = models.CharField(max_length=50)
    uni = models.CharField(max_length=50)


class Experience(models.Model):
    start_date = models.CharField(max_length=20)
    finish_date = models.CharField(max_length=20)
    post = models.CharField(max_length=20)
    company = models.CharField(max_length=50)


class Skills(models.Model):
    title = models.CharField(max_length=20)

