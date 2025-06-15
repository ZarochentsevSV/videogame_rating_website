
def is_user(user):
    return user.filter(name='user').exist()

def is_editor(user):
    return user.filter(name='editor').exist()

def is_admin(user):
    return user.filter(name='admin').exist()

def is_banned(user):
    return user.filter(name='banned').exist()