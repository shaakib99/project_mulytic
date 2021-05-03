from .models import User

def user_authenticated(phone = '', email = ''):
    if phone.strip() == '' or email.strip() == '':
        return False
    try:
        user = User.objects.get(email = email, phone = phone)
        return user
    except:
        return False