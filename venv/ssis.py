from SSISdb import registeredUser

def userFound(username, password):
    if registeredUser(username,password):
        return True