from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView, CreateView, DeleteView
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from accounts.models import Classroom, Teacher, User, Section, Resource, Assignment, AssignmentSubmission
from .forms import ClassroomForm, SectionForm, ResourceForm, AssignmentForm
from .mixins import TeacherTestMixin
import random

# Create your views here.

class DashboardView(TeacherTestMixin, TemplateView):
    template_name = "teachers/dashboard.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['classrooms'] = self.request.user.teachers.classrooms.all()
        return context

class ClassroomCreateView(CreateView):
    model = Classroom
    form_class = ClassroomForm
    template_name = "teachers/addclassroom.html"
    
    def form_valid(self, form):
        form.instance.teacher = self.request.user.teachers
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse('teachers:dashboard')
def event_list(request):
    return render(request, "teachers/event_list.html")

class ClassroomDeleteView(DeleteView):
    model = Classroom
    template_name = "teachers/deleteclassroom.html"
    slug_url_kwarg = 'code'
    slug_field = 'code'
    
    def get_success_url(self):
        return reverse('teachers:dashboard')

def ClassroomDetailView(request, code):
    context_dict = {}
    room = get_object_or_404(Classroom, code=code)
    context_dict['classroom'] = room
    return render(request, 'teachers/classroom_detail.html', context=context_dict)

class SectionCreateView(CreateView):
    model = Section
    form_class = SectionForm
    template_name = "teachers/add_section.html"

    def form_valid(self, form):
        form.instance.classroom = get_object_or_404(Classroom, code=self.kwargs['code'])
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse('teachers:classroom_detail', kwargs={'code': self.kwargs['code']})

class SectionDeleteView(DeleteView):
    model = Section
    template_name = "teachers/delete_section.html"
    
    def get_success_url(self):
        return reverse('teachers:classroom_detail', kwargs={'code': self.object.classroom.code})

def ResourcesView(request, pk):
    context_dict = {}
    section = get_object_or_404(Section, pk=pk)
    context_dict['section'] = section
    return render(request, 'teachers/resources.html', context=context_dict)

class ResourceCreateView(CreateView):
    model = Resource
    form_class = ResourceForm
    template_name = "teachers/add_resource.html"
    
    def form_valid(self, form):
        form.instance.section = get_object_or_404(Section, pk=self.kwargs['pk'])
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse('teachers:resources', kwargs={'pk': self.kwargs['pk']})

class ResourceDeleteView(DeleteView):
    model = Resource
    template_name = "teachers/delete_resource.html"
   
    def get_success_url(self):
        return reverse('teachers:resources', kwargs={'pk': self.object.section.pk})

def AssignmentsView(request, pk):
    context_dict = {}
    section = get_object_or_404(Section, pk=pk)
    context_dict['section'] = section
    return render(request, 'teachers/assignments.html', context=context_dict)

class AssignmentCreateView(CreateView):
    model = Assignment
    form_class = AssignmentForm
    template_name = "teachers/add_assignment.html"
    
    def form_valid(self, form):
        form.instance.section = get_object_or_404(Section, pk=self.kwargs['pk'])
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse('teachers:assignments', kwargs={'pk': self.kwargs['pk']})

class AssignmentDeleteView(DeleteView):
    model = Assignment
    template_name = "teachers/delete_assignment.html"
   
    def get_success_url(self):
        return reverse('teachers:assignments', kwargs={'pk': self.object.section.pk})

def AssignmentSubmissionsView(request, pk):
    context_dict = {}
    assignment = get_object_or_404(Assignment, pk=pk)
    context_dict['assignment'] = assignment
    context_dict['assignment_submissions'] = AssignmentSubmission.objects.filter(assignment=assignment)
    return render(request, 'teachers/submissions.html', context=context_dict)

def ClassroomStudentsView(request, code):
    context_dict = {}
    classroom = get_object_or_404(Classroom, code=code)
    context_dict['classroom'] = classroom
    context_dict['classroom_students'] = classroom.students.all()
    return render(request, 'teachers/classroomstudents.html', context=context_dict)

class CreateMeetingView(View):
    template_name = 'teachers/meeting.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        title = request.POST.get('title')
        date = request.POST.get('date')
        time = request.POST.get('time')
        # Save the meeting details to the database here
        # Example: Meeting.objects.create(title=title, date=date, time=time, teacher=request.user.teachers)
        return redirect(reverse('teachers:dashboard'))

class MeetingRoomView(View):
    template_name = 'teachers/meeting.html'

    def get(self, request, *args, **kwargs):
        room_id = kwargs.get('room_id')
        return render(request, self.template_name, context={'room_id': room_id})
