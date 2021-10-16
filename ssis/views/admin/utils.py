from ssis.models.admin import Admin

def admin_found(username: str, password: str) -> bool:
    if Admin(username,password).registered_user():
        return True


def verified(username: str = None, password: str = None, password2: str = None) -> bool:
    if username not in Admin().get_usernames() and password == password2:
        Admin(username,password).register()
        return True