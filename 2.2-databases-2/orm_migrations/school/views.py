from django.views.generic import ListView
from django.shortcuts import render
from django.http import HttpResponse

from .models import Student, Teacher


def students_list(request):
    template = 'school/students_list.html'
    student_obj = Student.objects.all()
    context = {'object_list':student_obj}
    # используйте этот параметр для упорядочивания результатов
    # https://docs.djangoproject.com/en/2.2/ref/models/querysets/#django.db.models.query.QuerySet.order_by
    ordering = 'group'
    return render(request, template, context)
