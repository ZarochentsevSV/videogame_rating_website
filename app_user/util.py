from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin

#user functions
def is_user(user):
    return user.groups.filter(name='user').exists()

def is_editor(user):
    return user.groups.filter(name='editor').exists()

def is_admin(user):
    return user.groups.filter(name='admin').exists()

def is_banned(user):
    return user.groups.filter(name='banned').exists()

#user classes
class IsInStaffCheckMixin(LoginRequiredMixin, UserPassesTestMixin):
    def test_func(self):
        return is_admin(self.request.user)|is_editor(self.request.user)

class IsUserAllowedCheckMixin(LoginRequiredMixin, UserPassesTestMixin):
    def test_func(self):
        return not is_banned(self.request.user)
