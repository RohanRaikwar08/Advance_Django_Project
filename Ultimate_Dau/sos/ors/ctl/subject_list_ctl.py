from django.shortcuts import render, redirect
from ..service.subject_service import SubjectService
from .base_ctl import BaseCtl


class SubjectListCtl(BaseCtl):

    def request_to_form(self, request):
        self.form['name'] = request.POST.get('name')

    def display(self, request, params={}):

        subject_list = self.get_service().search(self.form)
        self.form['list'] = subject_list
        return render(request, self.get_template(), {'form': self.form})

    def submit(self, request, params={}):

        self.request_to_form(request)

        if request.POST.get('operation', '') == "next":
            self.form['page_no'] = int(request.POST['pageNo'])
            self.form['page_no'] += 1
        if request.POST.get('operation', '') == "previous":
            self.form['page_no'] = int(request.POST['pageNo'])
            self.form['page_no'] -= 1
        if request.POST.get('operation', '') == "search":
            self.form['page_no'] = 1

        subject_list = self.get_service().search(self.form)
        self.form['list'] = subject_list

        return render(request, self.get_template(), {"form": self.form})

    def get_service(self):
        return SubjectService()

    def get_template(self):
        return 'subject_list.html'
