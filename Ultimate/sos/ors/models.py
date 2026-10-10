from django.db import models


class DropdownItem:
    def get_key(self):
        raise NotImplementedError

    def get_value(self):
        raise NotImplementedError


class User(DropdownItem, models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    login_id = models.CharField(max_length=50)
    password = models.CharField(max_length=20)
    dob = models.DateField(max_length=20)
    address = models.CharField(max_length=50)
    gender = models.CharField(max_length=50, default='')
    role_id = models.IntegerField()
    role_name = models.CharField(max_length=50)

    def get_key(self):
        return self.id

    def get_value(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        db_table = 'sos_user'


class Role(DropdownItem, models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)

    def get_key(self):
        return self.id

    def get_value(self):
        return self.name

    class Meta:
        db_table = "sos_role"


class Collage(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=20)

    class Meta:
        db_table = 'sos_college'


class Course(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    duration = models.CharField(max_length=100)

    class Meta:
        db_table = 'sos_course'


class Subject(DropdownItem, models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    course_id = models.IntegerField()
    course_name = models.CharField(max_length=50)

    class Meta:
        db_table = 'sos_subject'
