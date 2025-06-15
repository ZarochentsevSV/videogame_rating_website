
def is_user(user):
    return user.groups.filter(name='user').exists()

def is_editor(user):
    return user.groups.filter(name='editor').exists()

def is_admin(user):
    return user.groups.filter(name='admin').exists()

def is_banned(user):
    return user.groups.filter(name='banned').exists()