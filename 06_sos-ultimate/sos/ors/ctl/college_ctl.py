from .base_ctl import BaseCtl
from django.shortcuts import render

from ..models import College
from ..service.college_service import CollegeService
from ..utility.data_validator import DataValidator


class CollegeCtl(BaseCtl):

    def request_to_form(self, request):

        id = request.POST.get('id')

        if id == '' or id is None:
            self.form['id'] = 0
        else:
            self.form['id'] = int(id)

        self.form['name'] = request.POST.get('name')
        self.form['address'] = request.POST.get('address')
        self.form['state'] = request.POST.get('state')
        self.form['city'] = request.POST.get('city')
        self.form['phone_number'] = request.POST.get('phone_number')

        print("FORM =", self.form)

    def form_to_model(self, obj):
        obj.id = self.form['id']
        obj.name = self.form['name']
        obj.address = self.form['address']
        obj.state = self.form['state']
        obj.city = self.form['city']
        obj.phone_number = self.form['phone_number']

        print("MODEL =", obj.name, obj.address, obj.state, obj.city, obj.phone_number)
        return obj

    def model_to_form(self, obj):
        if (obj == None):
            return
        self.form['id'] = obj.id
        self.form['name'] = obj.name
        self.form['address'] = obj.address
        self.form['state'] = obj.state
        self.form['city'] = obj.city
        self.form['phone_number'] = obj.phone_number

    def input_validation(self, request):
        input_error = self.form.get("input_error")
        input_error['error'] = False

        if DataValidator.is_null(self.form['name']):
            input_error['name'] = 'Name is required'
            input_error['error'] = True

        if DataValidator.is_null(self.form['address']):
            input_error['address'] = 'Address is required'
            input_error['error'] = True

        if DataValidator.is_null(self.form['state']):
            input_error['state'] = 'State is required'
            input_error['error'] = True

        if DataValidator.is_null(self.form['city']):
            input_error['city'] = 'City is required'
            input_error['error'] = True

        if DataValidator.is_null(self.form['phone_number']):
            input_error['phone_number'] = 'Phone Number is required'
            input_error['error'] = True

        return input_error['error']

    def display(self, request, params={}):
        return render(request, self.get_template(), {'form': self.form})

    def submit(self, request, params={}):
        try:
            college = self.form_to_model(College())
            self.get_service().save(college)
            if self.form['id'] > 0:
                self.form['message'] = 'College Updated Successfully...!!!'
            else:
                self.form['message'] = 'College Added Successfully...!!!'
        except Exception as e:
            self.form['message'] = str(e)
            self.form['error'] = True
        return render(request, self.get_template(), {'form': self.form, "preload_data": self.preload(request)})

    def get_template(self):
        return "college.html"

    def get_service(self):
        return CollegeService()
