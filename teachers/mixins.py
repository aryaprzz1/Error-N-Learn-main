from django.contrib.auth.mixins import UserPassesTestMixin

class TeacherTestMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.teachers is not None
