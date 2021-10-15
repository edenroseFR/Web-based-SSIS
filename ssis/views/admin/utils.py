from ssis.models.admin import Admin

def admin_found(username, password):
    if Admin(username,password).registered_user():
        return True


def verified(username=None, password=None, password2=None):
    if username not in Admin().get_usernames() and password == password2:
        Admin(username,password).register()
        return True