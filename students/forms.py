from accounts.models import AssignmentSubmission
from django import forms

class AssignmentSubmissionForm(forms.ModelForm):
    class Meta:
        model = AssignmentSubmission
        fields = ("file",)

class JoinClassroomForm(forms.Form):
    code = forms.CharField(max_length=50, required=True)

class JoinMeetingForm(forms.Form):
    roomID = forms.CharField(
        max_length=100, 
        required=True, 
        widget=forms.TextInput(attrs={'placeholder': 'Room ID:', 'class': 'form-control'})
    )
