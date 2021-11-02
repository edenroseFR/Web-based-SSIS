from ssis.models.admin import Admin
from werkzeug.security import generate_password_hash

def admin_found(username: str, password: str) -> bool:
    if Admin(username,password).registered_user():
        return True
    return False

