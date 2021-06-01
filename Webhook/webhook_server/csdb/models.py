from aptdaemon.enums import _
from django.db import models

# Create your models here.


class Member(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=30, blank=False)
    email = models.CharField(max_length=50)
    IDENTITY_TYPE = (
        ('student', 'student'),
        ('professor', 'professor'),
        ('assistance', 'assistance')
    )
    identity = models.CharField(choices=IDENTITY_TYPE, max_length=10, default=IDENTITY_TYPE[0])
    phone = models.CharField(max_length=20, null=True)


class Account(models.Model):
    account_id = models.CharField(max_length=20, blank=False, primary_key=True)
    password = models.CharField(max_length=20, blank=False)
    RIGHT_TYPE = (
        (0, 'high'),
        (1, 'middle'),
        (2, 'low')
    )
    right = models.IntegerField(choices=RIGHT_TYPE, default=RIGHT_TYPE[2])
    last_login_date = models.DateTimeField(blank=True)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)


class File(models.Model):
    f_id = models.BigAutoField(primary_key=True)
    file_addr = models.CharField(max_length=50)
    upload_date = models.DateTimeField(blank=True)
    FILE_TYPE = (
        ('bachelor', 'bachelor'),
        ('master', 'master'),
        ('law', 'law')
    )
    type = models.CharField(choices=FILE_TYPE, max_length=10)
    account = models.ForeignKey(Account, on_delete=models.PROTECT)


class Student(Member):
    DEGREE_TYPE = (
        ('bachelor', 'bachelor'),
        ('master', 'master')
    )
    degree = models.CharField(choices=DEGREE_TYPE, max_length=10, blank=False)
    stu_id = models.CharField(max_length=10, blank=False)
    lab = models.CharField(max_length=20, null=True)


class Professor(Member):
    photo = models.CharField(max_length=30)
    lab = models.CharField(max_length=20, null=True)
    web = models.CharField(max_length=50, null=True)
    FULL_TIME_TYPE = (
        (2, 'full_time'),
        (1, 'concurrent'),
        (0, 'retire')
    )
    full_time = models.IntegerField(choices=FULL_TIME_TYPE, blank=False)


class Assistance(Member):
    pass


class Experience(models.Model):
    pro_id = models.ForeignKey(Professor, models.CASCADE, primary_key=True)
    content = models.CharField(max_length=50, blank=False)


class Skills(models.Model):
    pro_id = models.ForeignKey(Professor, models.CASCADE, primary_key=True)
    skill = models.CharField(max_length=50, blank=False)


class background(models.Model):
    pro_id = models.ForeignKey(Professor, models.CASCADE, primary_key=True)
    school = models.CharField(max_length=30, blank=False)
    department = models.CharField(max_length=30, blank=True)


class BachelorFile(File):
    pass


class MasterFile(File):
    class Category(models.TextChoices):
        ORAL = 'oral', _('oral')
        FORM = 'form', _('form')

    master_category = models.CharField(choices=Category.choices, max_length=4)


class LawFile(File):
    class Category(models.TextChoices):
        BACHELOR_LAW = 'BL', _('bachelor_law')
        MASTER_LAW = 'ML', _('master_law')
        ADMIN_LAW = 'AL', _('admin_law')

    law_category = models.CharField(choices=Category.choices, max_length=2)


class BachelorLaw(models.Model):
    f_id = models.ForeignKey(LawFile, models.CASCADE, primary_key=True)


class MasterLaw(models.Model):
    f_id = models.ForeignKey(LawFile, models.CASCADE, primary_key=True)


class AdminLaw(models.Model):
    f_id = models.ForeignKey(LawFile, models.CASCADE, primary_key=True)