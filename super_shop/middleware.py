from django.shortcuts import redirect
from django.urls import reverse

path_exception_in_reverse = [ 'shop-login', 'validate_login' ]
default_redirect_page_in_reverse = 'show_products'
default_login_page_in_reverse = 'shop-login'

def custom_auth_middleware(get_response):

    def check_if_accessing_authenticated_path(path, exception_path):
        for x in exception_path:
            if reverse(x) == path:
                return False
        return True

    def middleware(request):
        accessing_authenticated_path = check_if_accessing_authenticated_path(request.path, path_exception_in_reverse)
        
        # If user does not login but tries to access product or other authenticated page
        if request.session.get('uid') == None and accessing_authenticated_path: return redirect(default_login_page_in_reverse)
        
        # If user logged in but tries to access login page
        if request.session.get('uid') != None and not accessing_authenticated_path: return redirect(default_redirect_page_in_reverse)
        
        response = get_response(request)

        return response
        
    return middleware