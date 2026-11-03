from django.shortcuts import render, redirect

from .base_ctl import BaseCtl
from ..models import Faculty, Collage, Subject
from ..service.subject_service import SubjectService
from ..service.course_service import CourseService
from ..service.collage_service import CollageService
from ..service.faculty_service import FacultyService
from ..utility.data_validator import DataValidator
from ..utility.html_utility import HtmlUtility


class FacultyCtl(BaseCtl):

    def preload(self, request):
        gender_list = ["Male", "Female"]
        subject_list = SubjectService().search({})
        course_list = CourseService().search({})
        collage_list = CollageService().search({})

        self.form['preload_list'] = subject_list
        self.form['preload_list'] = course_list
        self.form['preload_list'] = collage_list

        self.preload_data["gender_select"] = HtmlUtility.get_list_from_list(
            "gender",
            self.form.get("gender"),
            gender_list
        )

        self.preload_data["subject_select"] = HtmlUtility.get_list_from_beans(
            "subjectId",
            self.form.get("subject_id"),
            subject_list
        )

        self.preload_data["course_select"] = HtmlUtility.get_list_from_beans(
            "courseId",
            self.form.get("course_id"),
            course_list
        )

        self.preload_data["collage_select"] = HtmlUtility.get_list_from_beans(
            "collageId",
            self.form.get("collage_id"),
            collage_list
        )

        return self.preload_data

    def request_to_form(self, request):
        self.form['id'] = int(request.POST.get('id', 0))
        self.form['first_name'] = request.POST.get('firstName')
        self.form['last_name'] = request.POST.get('lastName')
        self.form['email'] = request.POST.get('email')
        self.form['password'] = request.POST.get('password')
        self.form['dob'] = request.POST.get('dob')
        self.form['address'] = request.POST.get('address')
        self.form['gender'] = request.POST.get('gender')
        self.form['course_id'] = int(request.POST.get('courseId', 0))
        self.form['collage_id'] = int(request.POST.get('collageId', 0))
        self.form['subject_id'] = int(request.POST.get('subjectId', 0))

    def form_to_model(self, obj):
        obj.id = self.form['id']
        obj.first_name = self.form['first_name']
        obj.last_name = self.form['last_name']
        obj.email = self.form['email']
        obj.password = self.form['password']
        obj.dob = self.form['dob']
        obj.address = self.form['address']
        obj.gender = self.form['gender']
        obj.course_id = int(self.form['course_id'])
        obj.course_name = CourseService().get(self.form['course_id']).name
        obj.college_id = int(self.form['collage_id'])
        obj.college_name = CollageService().get(self.form['collage_id']).name
        obj.subject_id = int(self.form['subject_id'])
        obj.subject_name = SubjectService().get(self.form['subject_id']).name
        return obj

    def model_to_form(self, obj):
        self.form['id'] = obj.id
        self.form['first_name'] = obj.first_name
        self.form['last_name'] = obj.last_name
        self.form['email'] = obj.email
        self.form['password'] = obj.password
        self.form['dob'] = obj.dob.strftime('%Y-%m-%d')
        self.form['address'] = obj.address
        self.form['gender'] = obj.gender
        self.form['course_id'] = obj.course_id
        self.form['course_name'] = obj.course_name
        self.form['collage_id'] = obj.college_id
        self.form['collage_name'] = obj.college_name
        self.form['subject_id'] = obj.subject_id
        self.form['subject_name'] = obj.subject_name

    def input_validation(self, request):
        input_error = self.form['input_error']
        input_error['error'] = False
        if (DataValidator.is_null(request.POST.get("firstName", ''))):
            input_error['first_name'] = 'First Name is required'
            input_error['error'] = True
        if (DataValidator.is_null(request.POST.get("lastName", ''))):
            input_error['last_name'] = 'Last Name is required'
            input_error['error'] = True
        if (DataValidator.is_null(request.POST.get("email", ''))):
            input_error['email'] = 'Email ID is required'
            input_error['error'] = True
        if (DataValidator.is_null(request.POST.get("password", ''))):
            input_error['password'] = 'Password is required'
            input_error['error'] = True
        if (DataValidator.is_null(request.POST.get("dob", ''))):
            input_error['dob'] = 'DOB is required'
            input_error['error'] = True
        if (DataValidator.is_null(request.POST.get("address", ''))):
            input_error['address'] = 'Address is required'
            input_error['error'] = True

        if (DataValidator.is_null(self.form.get('gender')) or request.POST.get("gender") == "0"):
            input_error['gender'] = 'Gender is required'
            input_error['error'] = True

        if (DataValidator.is_null(self.form.get('subject_id')) or request.POST.get("subjectId") == "0"):
            input_error['subject_id'] = 'Subject is required'
            input_error['error'] = True

        if (DataValidator.is_null(self.form.get('course_id')) or request.POST.get("courseId") == "0"):
            input_error['course_id'] = 'Course is required'
            input_error['error'] = True

        if (DataValidator.is_null(self.form.get('collage_id')) or request.POST.get("collageId") == "0"):
            input_error['collage_id'] = 'Collage is required'
            input_error['error'] = True

        return input_error['error']

    def display(self, request, params={}):
        return render(request, self.get_template(), {'form': self.form, "preload_data": self.preload(request)})

    def submit(self, request, params={}):

        try:
            faculty = self.form_to_model(Faculty())
            self.get_service().save(faculty)
            if self.form['id'] > 0:
                self.form['message'] = 'Faculty Updated Successfully...!!!'
                self.form['error'] = False
            else:
                self.form['message'] = 'Faculty Added Successfully...!!!'
                self.form['error'] = False

        except Exception as e:
            self.form['message'] = str(e)
            self.form['error'] = True

        return render(request, self.get_template(), {'form': self.form, "preload_data": self.preload(request)})

    def get_service(self):
        return FacultyService()

    def get_template(self):
        return 'faculty.html'
