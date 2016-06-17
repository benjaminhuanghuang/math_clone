from functools import wraps
from flask_login import current_user
from flask import current_app
from permission import Permission

# Usage
# @required_roles('admin', 'user')
def requires_roles(*roles):
    def wrapper(f):
        @wraps(f)
        def wrapped(*args, **kwargs):
            if current_user.role not in roles:
                return current_app.login_manager.unauthorized()
            return f(*args, **kwargs)
        return wrapped
    return wrapper

def requires_permission(permission):
    def wrapper(f):
        @wraps(f)
        def wrapped(*args, **kwargs):
            if current_user.role < permission:
                return current_app.login_manager.unauthorized()
            return f(*args, **kwargs)
        return wrapped
    return wrapper



# def permission_required():
#
#
# def admin_required(f):
#     def wrapper(f):
#         @wraps(f)
#         def wrapped(*args, **kwargs):
#             if current_user.role not in roles:
#                 return error_response()
#             return f(*args, **kwargs)
#         return wrapped
#     return wrapper