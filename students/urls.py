from django.urls import path
from .views import (
    DashboardView,
    ClassroomDetailView,
    ResourcesView,
    AssignmentsView,
    AssignmentSubmissionCreateView,
    MyAssignmentView,
    AssignmentSubmissionDeleteView,
    joinClassroomView,
    LeaveClassroomView,
    event_list,
    JoinMeetingView,
    MeetingRoomView,
)

app_name = "students"

urlpatterns = [
    path("", DashboardView.as_view(), name="dashboard"),
    path("classroom/<slug:code>/", ClassroomDetailView, name="classroom_detail"),
    path("section/<int:pk>/resources/", ResourcesView, name="resources"),
    path("section/<int:pk>/assignments/", AssignmentsView, name="assignments"),
    path("assignment/<int:pk>/", MyAssignmentView, name="my_assignment"),
    path(
        "assignment/<int:pk>/submit/",
        AssignmentSubmissionCreateView.as_view(),
        name="submit_assignment",
    ),
    path(
        "delete-submission/<int:pk>/",
        AssignmentSubmissionDeleteView.as_view(),
        name="delete_submission",
    ),
    path("join-new/", joinClassroomView, name="join_classroom"),
    path("event_list/", event_list, name="event_list"),
    path("leave-classroom/<slug:code>/", LeaveClassroomView, name="leave_classroom"),
    path('join/', JoinMeetingView.as_view(), name='join'),
    path('meeting/<str:room_id>/', MeetingRoomView.as_view(), name='meeting_room'),
]
