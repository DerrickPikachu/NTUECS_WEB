# from aptdaemon.enums import _
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
    identity = models.CharField(choices=IDENTITY_TYPE, max_length=10, default=IDENTITY_TYPE[0][0])
    phone = models.CharField(max_length=20, null=True)


class Account(models.Model):
    account_id = models.CharField(max_length=20, blank=False, primary_key=True)
    password = models.CharField(max_length=20, blank=False)
    RIGHT_TYPE = (
        (0, 'high'),
        (1, 'middle'),
        (2, 'low')
    )
    right = models.IntegerField(choices=RIGHT_TYPE, default=RIGHT_TYPE[2][0])
    last_login_date = models.DateTimeField(null=True)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)


class File(models.Model):
    f_id = models.BigAutoField(primary_key=True)
    file_addr = models.CharField(max_length=50)
    upload_date = models.DateTimeField(null=True)
    FILE_TYPE = (
        ('bachelor', 'bachelor'),
        ('master', 'master'),
        ('law', 'law')
    )
    type = models.CharField(choices=FILE_TYPE, max_length=10, default=FILE_TYPE[0][0])
    account = models.ForeignKey(Account, on_delete=models.PROTECT)


class Student(Member):
    DEGREE_TYPE = (
        ('bachelor', 'bachelor'),
        ('master', 'master')
    )
    degree = models.CharField(choices=DEGREE_TYPE, max_length=10, blank=False, default=DEGREE_TYPE[0][0])
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
    full_time = models.IntegerField(choices=FULL_TIME_TYPE, blank=False, default=FULL_TIME_TYPE[0][0])


class Assistance(Member):
    pass


class Experience(models.Model):
    pro_id = models.ForeignKey(Professor, models.CASCADE)
    content = models.CharField(max_length=50, blank=False)


class Skills(models.Model):
    pro_id = models.ForeignKey(Professor, models.CASCADE)
    skill = models.CharField(max_length=50, blank=False)


class background(models.Model):
    pro_id = models.ForeignKey(Professor, models.CASCADE)
    school = models.CharField(max_length=30, blank=False)
    department = models.CharField(max_length=30, null=True)


class BachelorFile(File):
    pass


class MasterFile(File):
    class Category(models.TextChoices):
        ORAL = 'oral', 'oral'
        FORM = 'form', 'form'

    master_category = models.CharField(choices=Category.choices, max_length=4, default=Category.FORM)


class LawFile(File):
    class Category(models.TextChoices):
        BACHELOR_LAW = 'BL', 'bachelor_law'
        MASTER_LAW = 'ML', 'master_law'
        ADMIN_LAW = 'AL', 'admin_law'

    law_category = models.CharField(choices=Category.choices, max_length=2, default=Category.BACHELOR_LAW)


class BachelorLaw(models.Model):
    f_id = models.ForeignKey(LawFile, models.CASCADE)


class MasterLaw(models.Model):
    f_id = models.ForeignKey(LawFile, models.CASCADE)


class AdminLaw(models.Model):
    f_id = models.ForeignKey(LawFile, models.CASCADE)


class Announcement(models.Model):
    class Type(models.TextChoices):
        ANNOUNCE = 'AN', 'announce'
        CONGRATS = 'CO', 'congrats'
        SUPER_CONGRATS = 'SC', 'super_congrats'
    announce_text = models.CharField(max_length=50, null=False)
    announce_type = models.CharField(choices=Type.choices, max_length=2, default=Type.ANNOUNCE)
    account_id = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True)
    f_id = models.ForeignKey(File , on_delete=models.SET_NULL, null=True)