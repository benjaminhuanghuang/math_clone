from flask import render_template, request, redirect, url_for, current_app
from flask_login import login_required

from . import management
from app.models.user import User
from app.permission_control.decorators import requires_permission
from app.permission_control.permission import Permission


@management.route('/usermanagement')
@login_required
@requires_permission(Permission.ADMINISTER)
def usermanagement():
    users = User.get_all_users()
    return render_template('management/userlist.html', users=users)


@management.route('/userdetail')
@login_required
@requires_permission(Permission.ADMINISTER)
def user_detail():
    return render_template('management/user_detail.html')
