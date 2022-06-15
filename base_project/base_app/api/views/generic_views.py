from django.shortcuts import render
from django.views.generic.list import ListView
from ...models import EmployeeInfo



class EmployeeListView(ListView):
    template_name = 'employeeinfo_list.html'
    model = EmployeeInfo
    ordering = 'name'
    context_object_name = 'emp_data'

    def get_queryset(self):
        return EmployeeInfo.objects.filter(roll = 2)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['fresher'] = EmployeeInfo.objects.all().order_by('roll')
        return context
