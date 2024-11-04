from django.urls import path
from .views import (DashboardView, 
                    ClassroomCreateView, 
                    ClassroomDeleteView, 
                    ClassroomDetailView, 
                    ResourcesView,
                    SectionCreateView,
                    AssignmentsView,
                    SectionDeleteView,
                    ResourceCreateView,
                    ResourceDeleteView,
                    AssignmentCreateView,
                    AssignmentDeleteView,
                    AssignmentSubmissionsView,
                    ClassroomStudentsView,
                    CreateMeetingView,
                    event_list,
                    MeetingRoomView  # Make sure to import MeetingRoomView
                )

app_name = 'teachers'

urlpatterns = [
    path('',                                DashboardView.as_view(),        name='dashboard'),
    path('classroom/add/',                  ClassroomCreateView.as_view(),  name='add_classroom'),
    path('classroom/<slug:code>/delete/',   ClassroomDeleteView.as_view(),  name='delete_classroom'),
    path('classroom/<slug:code>/',          ClassroomDetailView,            name='classroom_detail'),
    path('classroom/<slug:code>/students/', ClassroomStudentsView,          name='classroom_students'),
    path('classroom/<slug:code>/add/',      SectionCreateView.as_view(),    name='add_section'),
    path('section/<int:pk>/delete/',        SectionDeleteView.as_view(),    name='delete_section'),
    path('resources/<int:pk>/',             ResourcesView,                  name='resources'),
    path('resources/<int:pk>/add/',         ResourceCreateView.as_view(),   name='add_resource'),
    path('resources/delete/<int:pk>/',      ResourceDeleteView.as_view(),   name='delete_resource'),
    path('assignments/<int:pk>/',           AssignmentsView,                name='assignments'),
    path('assignments/<int:pk>/add/',       AssignmentCreateView.as_view(), name='add_assignment'),
    path('assignments/delete/<int:pk>/',    AssignmentDeleteView.as_view(), name='delete_assignment'),
    path('submissions/<int:pk>/',           AssignmentSubmissionsView,      name='assignment_submissions'),
    path('create_meeting/',                 CreateMeetingView.as_view(),    name='create_meeting'),
    path('meeting/',                       MeetingRoomView.as_view(),      name='meeting_room'), 
     path("event_list/", event_list, name="event_list"), # Added URL pattern for MeetingRoomView
]
