# Fonction qui va restreindre l'accès aux utilisateurs
# déjà connectés.

def user_not_authenticated(user):
    return not user.is_authenticated

def user_is_authenticated(user):
    return user.is_authenticated

def user_is_admin(user):
    return user.is_staff or user.superuser
