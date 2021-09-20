from SSISdb import registeredUser, existingUsernames, registerAdmin

def userFound(username, password):
    if registeredUser(username,password):
        return True

def verified(username=None, password=None, password2=None):
    if username not in existingUsernames() and password == password2:
        print('verified')
        registerAdmin(username,password)
        return True
