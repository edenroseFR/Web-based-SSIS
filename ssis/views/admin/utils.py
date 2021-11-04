from ssis.models.admin import Admin

def admin_found(username: str, password: str) -> bool:
    if Admin(username,password).registered_user():
        return True
    return False

